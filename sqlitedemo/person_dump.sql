PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE person (
    id int primary_key not null,
    name text not null,
    age  int 
);
INSERT INTO "person" VALUES(1,'Bob',22);
INSERT INTO "person" VALUES(2,'Sue',34);
INSERT INTO "person" VALUES(3,'Timmy',19);
INSERT INTO "person" VALUES(4,'Ellen',24);
COMMIT;
