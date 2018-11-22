#!/usr/bin/env python3.5
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2017 HunDunDM. All Rights Reserved
#
"""
Python3 Only...


@file: index.py
@Authors: HunDunDM (zhengxiangsheng@nenyatech.com)
@Date: 2017/2/6
"""

import os
import json
import argparse
import yaml as _yaml
import yaml.resolver as _yaml_resolver
from tornado.web import RequestHandler, HTTPError, Application
from tornado.ioloop import PeriodicCallback, IOLoop
from collections import OrderedDict

# region yaml

# libyaml若正常工作，性能更好
if _yaml.__with_libyaml__:
    from yaml import CSafeLoader as _yaml_SafeLoader
    from yaml import CSafeDumper as _yaml_SafeDumper
else:
    from yaml import SafeLoader as _yaml_SafeLoader
    from yaml import SafeDumper as _yaml_SafeDumper


# 输入dict全部转为OrderedDict以保持顺序
# 增加自定义!include !includes !join支持
class YamlLoader(_yaml_SafeLoader):
    # OrderedDict
    def construct_yaml_map(self, node):
        data = OrderedDict()
        yield data
        data.update(self.construct_pairs(node))

    # !include 「相似而区别于swagger的 $ref 」
    # 规定引用必须为绝对引用，需要load前显式设定root
    # 接受一个str，为文件绝对路径
    # 返回一个dict
    @classmethod
    def set_root(cls, root):
        cls.root = root

    def construct_include(self, node):
        assert hasattr(self, 'root')
        file = os.path.join(self.root, self.construct_scalar(node))
        return yaml_load(file, root=None)

    # !includes 「include多个文件」
    def construct_includes(self, node):
        assert hasattr(self, 'root')
        data = OrderedDict()
        file_list = self.construct_sequence(node, deep=True)
        for node in file_list:
            file = os.path.join(self.root, node)
            data.update(yaml_load(file, root=None))
        return data

    # !join 「相似而区别于swagger的 allOf 」
    # 接受一个list，要求元素为dict
    # 返回一个dict
    def construct_join(self, node):
        data = OrderedDict()
        subdata_list = self.construct_sequence(node, deep=True)
        for subdata in subdata_list:
            data.update(subdata)
        return data


YamlLoader.add_constructor(_yaml_resolver.BaseResolver.DEFAULT_MAPPING_TAG, YamlLoader.construct_yaml_map)
YamlLoader.add_constructor('!include', YamlLoader.construct_include)
YamlLoader.add_constructor('!join', YamlLoader.construct_join)
YamlLoader.add_constructor('!includes', YamlLoader.construct_includes)


def yaml_load(file, root='.'):
    if root is not None:
        YamlLoader.set_root(root)
        file = os.path.join(root, file)
    with open(file, 'r', encoding='utf-8') as ifs:
        return _yaml.load(ifs, YamlLoader)


# 输出支持OrderedDict，视为dict类型，并且输出时按照顺序
class YamlDumper(_yaml_SafeDumper):
    def represent_ordered_dict(self, data):
        return self.represent_dict(data.items())


YamlDumper.add_representer(OrderedDict, YamlDumper.represent_ordered_dict)


# 输出函数，格式化输出
# 返回bytes类型
def yaml_dump(data, file_name=None):
    if file_name is None:
        return _yaml.dump(data, Dumper=YamlDumper, encoding='utf-8', default_flow_style=False, allow_unicode=True)
    else:
        with open(file_name, 'w', encoding='utf-8', newline='\n') as ofs:
            _yaml.dump(data, ofs, YamlDumper, default_flow_style=False, allow_unicode=True)


# endregion


# region json

# 返回bytes类型
def json_dump(data, file_name=None):
    if file_name is None:
        return json.dumps(data, ensure_ascii=False).encode()
    else:
        with open(file_name, 'w', encoding='utf-8', newline='\n') as ofs:
            json.dump(data, ofs, ensure_ascii=False)


# endregion


# region web

class MainHandler(RequestHandler):
    mime_json = "application/json"
    mime_jsonu8 = "application/json; charset=UTF-8"
    mime_yaml = "text/x-yaml"
    mime_yamlu8 = "text/x-yaml; charset=UTF-8"
    default_mime = mime_yamlu8

    def data_received(self, chunk):
        """消除继承warning，该方法为stream模式下需要的方法，本项目中禁止使用
        """
        pass

    def initialize(self, workspace='.'):
        self.workspace = workspace

    def options(self, *args, **kwargs):
        pass

    def set_default_headers(self):
        """允许跨域"""
        self.set_header('Access-Control-Allow-Origin', self.request.headers.get("Origin", "*"))
        self.set_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Headers', 'Accept, Origin')
        self.set_header('Cache-Control', 'no-store')

    def reply(self, data=None):
        # 无数据则直接返回
        if data is None:
            self.clear_header("Content-Type")
            self.finish()
            return
        # 获取返回类型
        accept_content_type = None
        # 指定文件名后缀则按后缀返回
        file_type = self.path_kwargs.get("file_type")
        if file_type == 'json':
            accept_content_type = self.mime_jsonu8
        elif file_type == 'yaml':
            accept_content_type = self.mime_yamlu8
        # 否则按header的Accept字段返回，默认yaml
        if accept_content_type is None:
            content_type = self.request.headers.get('Accept', self.default_mime)
            if content_type.startswith(self.mime_json):
                accept_content_type = self.mime_jsonu8
            else:
                accept_content_type = self.default_mime
        # 根据返回类型序列化数据
        if accept_content_type == self.mime_yamlu8:
            chunk = yaml_dump(data)
        elif accept_content_type == self.mime_jsonu8:
            chunk = json_dump(data)
        else:
            raise HTTPError(403)
        self.set_header("Content-Type", accept_content_type)
        self.finish(chunk)

    def get(self, base_path, namespace, file_name='index', file_type='yaml'):
        file = os.path.join(namespace, '{0}.yaml'.format(file_name))
        if not os.path.exists(os.path.join(self.workspace, file)):
            raise HTTPError(404)
        data = yaml_load(file, self.workspace)
        solve(data, base_path)  # 根据base_path外部处理
        self.reply(data)


def create_app(workspace,
               namespace_list,
               file_name_list=None,
               file_type_list=None,
               base_path_list=None,
               debug=False):
    file_name_list = file_name_list or ('index',)
    file_type_list = file_type_list or ('yaml', 'json')
    base_path_list = base_path_list or ('r', 'd', 'l')

    namespace_rex = r"(?P<namespace>%s)" % '|'.join(namespace_list)
    file_name_rex = r"(?P<file_name>%s)" % '|'.join(file_name_list)
    file_type_rex = r"(?P<file_type>%s)" % '|'.join(file_type_list)
    base_path_rex = r"(?P<base_path>%s)" % '|'.join(base_path_list)

    url_rex_list = (
        r"/%s/%s" % (base_path_rex, namespace_rex),
        r"/%s/%s\.%s" % (base_path_rex, namespace_rex, file_type_rex),
        r"/%s/%s/%s" % (base_path_rex, namespace_rex, file_name_rex),
        r"/%s/%s/%s\.%s" % (base_path_rex, namespace_rex, file_name_rex, file_type_rex),
    )

    return Application(
        [(url_rex, MainHandler, dict(workspace=workspace)) for url_rex in url_rex_list],
        debug=debug,
    )


# endregion


# region main

_parser = argparse.ArgumentParser(prog='python index.py', description='Tmind Doc Server.')
_parser.add_argument("-D", "--debug", dest='debug', action='store_true',
                     help="run server in debug state")
_parser.add_argument("-P", "--port", dest='port', action='store',
                     help="server port")
_args = _parser.parse_args()


# 配置服务地址
def solve(data, base_path):
    if base_path == 'd':
        data['host'] = 'apitest.tmindtech.com'
        data['basePath'] = '/lawcat/dev/v1'
    elif base_path == 't':
        data['host'] = 'apitest.tmindtech.com'
        data['basePath'] = '/lawcat/test/v1'
    elif base_path == 'l':
        data['schemes'] = ['http']  # 本地环境不使用https
        data['host'] = '127.0.0.1:8080'  # 使用8080端口，规避80端口需要root权限

class Main:
    workspace = 'tmindtech'

    namespace_list = (
        'account',
        'auth',
        'storage',
        'user',
     )

    base_path_list = (
        'l',  # 本地环境 local
        't',  # 测试环境 test
        'd',  # 开发环境 dev
    )

    def run(self):
        app = create_app(self.workspace, self.namespace_list, base_path_list=self.base_path_list, debug=_args.debug)
        port = '9876' if not _args.port else _args.port
        app.listen(port, "" if _args.debug else '127.0.0.1')
        ioloop = IOLoop.current()
        PeriodicCallback(lambda: None, 500, ioloop).start()
        for name in self.namespace_list:
            print("http://swagger.tmindtech.com/?url=http://localhost:%s/l/%s" % (port, name))
        ioloop.start()


if __name__ == '__main__':
    Main().run()

# endregion
