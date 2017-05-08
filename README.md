# API设计基础项目
本项目用于提供API设计初始模板

新的API设计项目可以从本项目Fork后展开

## Feature
| 功能 | 工具 | 展示 |
| --- | --- | --- |
| UML Diagram | Plantuml | Gitlab |
| API Define | Swagger Open API | Swagger UI |

# 如何使用
## To 后端开发
* 参考usecase等uml理解设计的逻辑
* 参考class diagram生成数据库定义
* 参考API实现功能

## To 前端开发
* 参考API完成和后端的对接

## 测试服务地址
提供测试用的Swagger UI地址

[example](http://swagger.tmindtech.com/?url=https://apitest.tmindtech.com/base/doc/d/example)

# 如何开始
## 开发环境
### IDE
PyCharm

### 插件
plantuml

markdown

### 涉及语言
* plantuml
    * 用于UML图形绘制
    * 要求精通
* yaml
    * 用于API定义
    * 要求精通
* python 
    * 用于提供API文档的分文件支持
    * 要求了解

## 设计指引
* 通过需求分析, 生成usecase 
    * 必要时提供其他uml进行说明, 比如组件图, 状态图, 时序图
* 按照Restful风格定义生成API文档
* 通过class diagram生成数据库的定义

## UML
[uml-readme.md](./uml-readme.md)

## API
[api-readme.md](./api-readme.md)
