create table species (
	id int primary_key not null,
	name text
);

create table breed (
	id int primary_key not null,
	name text,
	species_id int
);

create table pet (
	id int primary_key not null,
	name text,
	adopted int,
	dead int,
	breed_id int
);

create table person (
	id int primary_key not null,
	first_name text,
	last_name text,
	age int,
	email text,
	phone text
);

create table person_pet (
	person_id int,
	pet_id int
);

insert into species (id, name) values 
	(1, "Cat"),
	(2, "Dog"),
	(3, "Rabbit")
;

insert into breed (id, name, species_id) values
	(1, "Abyssinian", 1),
	(2, "Bombay", 1),
	(3, "Persian", 1),
	(4, "Akita", 2),
	(5, "German Shepherd", 2),
	(6, "St. Bernard", 2),
	(7, "Californian", 3),
	(8, "Dutch", 3),
	(9, "Palomino", 3)
;

insert into pet (id, name, adopted, dead, breed_id) values
	(1, "Fluffy", 0, 0, 2),
	(2, "Patches", 1, 0, 2),
	(3, "Blinky", 0, 1, 5),
	(4, "Carl", 1, 1, 4),
	(5, "Zeus", 1, 0, 4),
	(6, "Mimi", 1, 0, 9)
;

insert into person (id, first_name, last_name, age, email, phone) values
	(1, "John", "Smith", 30, "jsmith@gmail.com", "555-1212"),
	(2, "Megan", "McAllister", 54, "Meg@hotmail.com", "324-453-2345"),
	(3, "Hannah", "Rahman", 23, "pinky@yahoo.com", "212-830-1234"),
	(4, "Patrick", "Bateman", 41, "cool@guy.com", "123-456-7890")
;

insert into person_pet (person_id, pet_id) values
	(1, 4),
	(1, 5),
	(2, 2),
	(3, 6)
;



	
