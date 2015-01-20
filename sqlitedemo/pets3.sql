PRAGMA foreign_keys=ON;

CREATE TABLE shelter (
	id int primary_key not null,
	name text,
	address text,
	phone text,
	website text
);

ALTER TABLE pet ADD COLUMN shelter_id int REFERENCES shelter(id) ON DELETE SET NULL ON UPDATE CASCADE;
