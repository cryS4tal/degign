# API设计基础项目
本项目用于提供API设计初始模板

新的API设计项目可以从本项目Fork后展开

## Feature
| 功能 | 工具 | 展示 |
| --- | --- | --- |
| UML Diagram | Plantuml | Gitlab |
| API Define | Swagger Open API | Swagger UI |

## IDE
PyCharm

## 设计指引
* 通过需求分析, 生成usecase 
    * 必要时提供其他uml进行说明, 比如组件图, 状态图, 时序图
* 按照Restful风格定义生成API文档
* 通过class diagram生成数据库的定义

## To 后端开发
* 参考usecase等uml理解设计的逻辑
* 参考class diagram生成数据库定义
* 参考API实现功能

## To 前端开发
* 参考API完成和后端的对接

## UML
UML使用[plantuml][]进行书写
[plantuml]: http://plantuml.com/
> 依赖插件 plantuml

### 使用约定
#### 文件名
name.[diagram type].puml.md
* diagram type
> 用于表明图的类型

* puml.md
> 由于gitlab对于plantuml的展现是内嵌在markdown文件中进行呈现,
> 所以plantuml的文件定义需要使用md作为文件名的后缀,
> 同时为了正确区分md和plantuml使preview插件正确工作而采用"puml.md"

#### 格式

\`\`\`plantuml

@startuml 

此处为进行plantuml定义

@enduml

\`\`\`

## API
遵循Restful的设计规范, 以OpenAPI为载体, 通过Swagger UI进行展现

### swagger 网页UI端

[Tmind swagger-ui](swagger.tmindtech.com)

基于官方github分支，做了如下修改

* 修改扩展语言为中文
* 开启Cookies支持

### swagger 官方文档

[官网](http://swagger.io)

[如何使用yaml撰写swagger文档](http://swagger.io/specification/)
or [OAI github版](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md)

[官方UI端Github](https://github.com/swagger-api/swagger-ui)

### 附加规范
> 背景
* 文档原本支持在$ref中跨文件引用，但实际经常造成混乱和错误，且文档中大量出现跨文件引用时并不方便。

> 说明
* 最适合的文档类型为单页文档，即文档中不存在跨文档引用。
* 但实际项目的多个模块如果都放在一页中，则不便于维护。
* 如果每个模块自己一页文档，则存在大量冗余数据，依然不便于维护。
* 所以增加一层中间服务器，实际文档以项目形式编写，由服务器来生成最终的模块单页文档。

> 项目结构 (api目录)
* requirements.txt | python服务器pip依赖说明文件 `pip install -r requirements.txt`
* index.py | 服务器源码，实现了自定义操作，用于产出单页文档

> 自定义操作
* join: 接list，其元素为dict，将所有dict合并为一个dict，不允许key重复
* include: 接字符串，载入文件为dict
* includes: 接字符串list，载入文件列表「join多个include文件的简单写法」

> 规范
* 禁止：在$ref中禁止使用跨文件引用。
* 禁止：$ref禁止循环引用，会导致文档展开为无穷大。
* 禁止：include(s)禁止循环引用，请将他们合并为一个文件。
* 禁止：include(s)禁止重复引用。由于工作原理同C的include而非import，并且没有高端的宏，请谅解。
* 强制：缩进为2空格。
* 强制：RESTful。
* 强制：使用示例格式组织文件
	* index.yaml 定义文件说明和依赖 仅在此文件使用自定义操作
	* definitions.yaml 定义object
	* parameters.yaml 定义参数
	* responses.yaml 定义返回值
	* p_[model].yaml 定义API路由
* 强制: 所有的API参数要进行description
* 强制：列表的-号前缩进一级。
* 强制：url的左斜线符号/放在前面，不放在末尾。
* 推荐：join操作的key尽量不要重复。目前的逻辑是重复的key，后者value覆盖前者。
* 推荐：object的定义，如果存在重复部分，请多多使用allOf减少代码冗余，其逻辑类似多继承。
* 推荐：如果api的参数dict深度最深只有1层，推荐不要使用body型parameter，因为其说明不够清晰，且使用不够方便。
* 推荐：在需要用到引号的场合，尽可能使用双引号。

> 约定
* 需要登录的接口如果未登录则会返回401错误，文档中不再单独标出。
* 非搜索的get接口，如果资源不存在则会返回404错误，文档中不再单独标出。
* 没有权限或者Auth鉴权失败时会返回403错误，文档中不再标出。

> IDE环境

基础语言python，要求版本3.5+

package依赖为requirements.txt

推荐使用pyvenv建立虚拟环境

python index.py 启动

[PyYAML官网](http://pyyaml.org/wiki)

centos推荐额外安装libyaml，可提高性能`sudo yum install libyaml-devel`


