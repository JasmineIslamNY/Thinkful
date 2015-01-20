select * from pet where breed_id in 
	(select id from breed where species_id = (select id from species where name = "Cat"));
select * from pet;
update pet set adopted = 0 where breed_id in 
	(select id from breed where species_id = (select id from species where name = "Cat"));
select * from pet;
select person.first_name, person.last_name, pet.name from person, pet, person_pet where 
	(person_pet.person_id = person.id AND person_pet.pet_id = pet.id);
update pet set adopted = 1 where 
	id in (select pet.id from person, pet, person_pet where 
		(person_pet.person_id = person.id AND person_pet.pet_id = pet.id) and
			pet.breed_id in (select id from breed where species_id = (select id from species where name = "Cat"))
		);
select * from pet;
