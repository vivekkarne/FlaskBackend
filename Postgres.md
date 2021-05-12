CREATE TABLE products(
   id    SERIAL   PRIMARY KEY     NOT NULL,
   name  TEXT  NOT NULL,
   description TEXT
);

CREATE TABLE users(
   id    SERIAL   PRIMARY KEY     NOT NULL,
   name  TEXT  NOT NULL
);

locate bin/postgres
9.5.25-alpine