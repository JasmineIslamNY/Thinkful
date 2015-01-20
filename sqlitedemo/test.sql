select person.first_name, person.last_name, pet.name from person, pet, person_pet where 
	(person_pet.person_id = person.id AND person_pet.pet_id = pet.id);
