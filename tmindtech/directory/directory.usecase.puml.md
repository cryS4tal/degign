```plantuml
@startuml
left to right direction

module --> (list tree)
module --> (create node) : folder/file
module --> (delete node)
module --> (update node)

@enduml
```