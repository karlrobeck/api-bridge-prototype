CREATE TABLE APP (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL UNIQUE,
    DESCRIPTION TEXT NOT NULL,
    APP_WEBSITE TEXT NOT NULL,
    REDIRECT_URI TEXT NOT NULL,
    APP_TYPE TEXT NOT NULL,
    ROLE TEXT NOT NULL,
    SCOPE TEXT NOT NULL
);