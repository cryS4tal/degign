@startuml

object survey {
    Long id;

    String path;

    String name;

    String description;

    Boolean enabled;

    Long edition_id;

    Timestamp create_time;

    Timestamp modify_time;
}

object result {
    Long id;

    Long owner_id;

    Long survey_id;

    Long edition_id;

    String extras;

    Timestamp create_time;

    Timestamp modify_time;
}

object edition {
    Long id;

    Long survey_id;

    String extras;

    Boolean enabled;

    Timestamp create_time;

    Timestamp modify_time;
}


@enduml