# UML
UML使用[plantuml][]进行书写

[plantuml]: http://plantuml.com/
> 依赖插件 plantuml

## 使用约定
### 文件名
name.[diagram type].puml.md
* diagram type

用于表明图的类型

* puml.md

由于gitlab对于plantuml的展现是内嵌在markdown文件中进行呈现,

所以plantuml的文件定义需要使用md作为文件名的后缀,

同时为了正确区分md和plantuml使preview插件正确工作而采用"puml.md"

### 格式

\`\`\`plantuml

@startuml 

此处为进行plantuml定义

@enduml

\`\`\`

