CREATE TABLE products(
   id    SERIAL   PRIMARY KEY     NOT NULL,
   name  TEXT  NOT NULL,
   description TEXT
);

CREATE TABLE users(
   id    SERIAL   PRIMARY KEY     NOT NULL,
   name  TEXT  NOT NULL
);