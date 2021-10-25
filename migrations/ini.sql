CREATE TABLE Track (
    id integer PRIMARY KEY AUTOINCREMENT,
    project_ID INTEGER,
    start_time time,
    end_time time,
    project_time TEXT
);

CREATE TABLE Project (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)