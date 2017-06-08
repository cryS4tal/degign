@startuml

object survey {
    int64 id;

    string path;

    string name;

    string description;

    boolean enabled;

    int64 edition_id;

    datetime create_time;

    datetime modify_time;
}

object result {
    int64 id;

    int64 owner_id;

    int64 survey_id;

    int64 edition_id;

    string extras;

    datetime create_time;

    datetime modify_time;
}

object edition {
    int64 id;

    int64 survey_id;

    string extras;

    boolean enabled;

    datetime create_time;

    datetime modify_time;
}


@enduml