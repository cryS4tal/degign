```plantuml
@startuml
left to right direction

user --> (Get Comment List) : Survey Result
user --> (Add Plus) : Comment

lawyer --> (Get Comment List) : Survey Result
lawyer --> (Add Comment) : Survey Result

admin --> (Get Comment List) : Survey Result
@enduml
```