from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table
from sqlalchemy import update
from sqlalchemy import UniqueConstraint

import logging
log = logging.getLogger(__name__)

################################################################################
# set up logging - see: https://docs.python.org/2/howto/logging.html

# when we get to using Flask, this will all be done for us
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
log.addHandler(console_handler)


################################################################################
# Domain Model

Base = declarative_base()
log.info("base class generated: {}".format(Base) )

# define our domain model
class Species(Base):
    """
    domain model class for a Species
    """
    __tablename__ = 'species'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breeds = relationship('Breed', backref="species", cascade="all, delete-orphan")

    # methods
    def __repr__(self):
        return self.name                   

# our many-to-many association table, in our domain model *before* Breed class 
breed_traits_table = Table('breed_trait', Base.metadata,
    Column('breed_id', Integer, ForeignKey('breed.id'), nullable=False),
    Column('breedtrait_id', Integer, ForeignKey('breedtrait.id'), nullable=False)
)


class Breed(Base):
    """
    domain model class for a Breed
    has a with many-to-one relationship Species
    has a many-to-many relationship with BreedTraits
    """
    __tablename__ = 'breed'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False )            
    pets = relationship('Pet', backref="breed")
    
    # no foreign key here, it's in the many-to-many table        
    # mapped relationship, breed_traits_table must already be in scope!
    traits = relationship('BreedTrait', secondary=breed_traits_table, backref='breed')
    
    # methods
    def __repr__(self):
        return "{}: {}".format(self.name, self.species) 

class BreedTrait(Base):
    """
    domain model class for recording breed traits
    has a many-to-many relationship with Breed
    """
    __tablename__ = 'breedtrait'
    
    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # mapped relationship 'breed' from backref on Breed class, so we don't
    # need to add it here.
    
    def __repr__(self):
        return "Breed Trait:{}".format(self.name) 

class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    website = Column(Text)
    pets = relationship('Pet', backref="shelter")

    def __repr__(self):
        return "Shelter: {}".format(self.name) 

"""
taken care of by Class PetPersonAssociation
# our many-to-many association table, in our domain model *before* Pet class 
pet_person_table = Table('pet_person', Base.metadata,
    Column('pet_id', Integer, ForeignKey('pet.id'), nullable=False),
    Column('person_id', Integer, ForeignKey('person.id'), nullable=False)
)
"""

class PetPersonAssociation(Base):
    __tablename__ = 'pet_person_association'

    # Here we use __table_args__ along with UniqueConstraint
    # to ensure that the combo of pet_id and person_id is unique
    # You can search for these terms in the SQLAlchemy docs.
    __table_args__ = (
            UniqueConstraint('pet_id', 'person_id', name='person_pet_uniqueness_constraint'),
        )
    id = Column(Integer, primary_key=True)

    # the combination of the two columns below must be unique, because above
    # we have defined the UniqueConstraint above. We require both fields
    # below.
    pet_id = Column(Integer, ForeignKey('pet.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)

    # a string for capturing nicknames
    nickname = Column(String)

    person = relationship('Person', backref=backref('pet_associations') )
    pet = relationship('Pet', backref=backref('person_associations'))

    # note that we added a .full_name property to our person class
    # which concatenates first and last name.

    def __repr__(self):
        return "PetPersonAssociation( {} : {} )".format(self.pet.name, 
            self.person.full_name)
        
pet_parent_to_child = Table("pet_parent_to_child", Base.metadata,
    Column("parent_id", Integer, ForeignKey("pet.id"), primary_key=True),
    Column("child_id", Integer, ForeignKey("pet.id"), primary_key=True)
)

class Pet(Base):
    """
    domain model class for a Pet, which has a many-to-one relation with Shelter, 
    a many-to-one relation with breed, and a many-to-many relation with person
    """
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    adopted = Column(Boolean)
    breed_id = Column(Integer, ForeignKey('breed.id'), nullable=False ) 
    shelter_id = Column(Integer, ForeignKey('shelter.id') ) 
    #parent_id = Column(Integer, ForeignKey(id), nullable=True)
    
    #parent = relationship('Pet', remote_side=id, backref="children")
    # tried using _parent with the @parent.setter below
    parent = relationship("Pet",
                        secondary=pet_parent_to_child,
                        primaryjoin=id==pet_parent_to_child.c.child_id,
                        secondaryjoin=id==pet_parent_to_child.c.parent_id,
                        backref="children")
    
    # no foreign key here, it's in the many-to-many table        
    # mapped relationship, pet_person_table must already be in scope!
    people = relationship('Person', secondary=pet_person_association, backref='pets')
    """
    @parent.setter 
    def parent(self, value):
        #check to see if two parents already exist
        if count(self.parent) == 2:
            raise Exception("Two parents already exist")
        else:
            self._parent = value    
    """
    
    @property
    def nicknames(self):
        """returns pet nickname"""
        return [assoc.nickname for assoc in self.person_associations]

    def __repr__(self):
        return "Pet:{}".format(self.name) 



class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer)
    _phone = Column(String)

    # mapped relationship 'pets' from backref on Pet class, so we don't
    # need to add it here.

    @property
    def phone(self):
        """return phone number formatted with hyphens"""
        # get the phone number from the database, mapped to private self._phone
        num = self._phone
        # return a formatted version using hyphens
        return "%s-%s-%s" % (num[0:3], num[3:6], num[6:10])

    def full_name(self):
        """return full name of person"""
        return "{} {}".format(self.first_name, self.last_name)

    # phone number writing property, writing to public Person.phone calls this 
    @phone.setter 
    def phone(self, value):
        """store only numeric digits, raise exception on wrong number length"""
        # remove any hyphens
        number = value.replace('-', '')
        # remove any spaces
        number = number.replace(' ', '')
        # check length, raise exception if bad
        if len(number) != 10:
            raise Exception("Phone number not 10 digits long")
        else:
            # write the value to the property that automatically goes to DB
            self._phone = number

    def __repr__(self):
        return "Person: {} {}".format(self.first_name, self.last_name) 


################################################################################
def init_db(engine):
    "initialize our database, drops and creates our tables"
    log.info("init_db() engine: {}".format(engine) )
    
    # drop all tables and recreate
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    log.info("  - tables dropped and created")


if __name__ == "__main__":
    log.info("main executing:")              

    # create an engine
    engine = create_engine('sqlite:///:memory:')
    log.info("created engine: {}".format(engine) )

    # if we asked to init the db from the command line, do so
    if True:
        init_db(engine)

    # call the sessionmaker factory to make a Session class 
    Session = sessionmaker(bind=engine)
    
    # get a local session for the this script
    db_session = Session()
    log.info("Session created: {}".format(db_session) )
   

    # create two people: Tom and Sue
    log.info("Creating person object for Tom")
    tom = Person(first_name="Tom",
                last_name="Smith",
                age=52,
                phone = '555-555-5555')

    log.info("Creating person object for Sue")
    sue = Person(first_name="Sue",
                last_name="Johson",
                age=54,
                phone = '555 243 9988')


    # create two animals, and in process, new species, with two breeds.
    # Note how we only explicitly commit spot and goldie below, but by doing so
    # we also save our new people, breeds, and species.

    log.info("Creating pet object for Spot, who is a Dalmatian dog")
    spot = Pet(name = "Spot",
                age = 2,
                adopted = True,
                breed = Breed(name="Dalmatian", species=Species(name="Dog")),
                people = [tom, sue]
                )

    # now we set Spot's breed to a variable because we don't want to create
    # a duplicate record for Dog in the species table, which is what would 
    # happen if we created Dog on the fly again when instantiating Goldie
    dog = spot.breed.species

    log.info("Creating pet object for Goldie, who is a Golden Retriever dog")
    goldie = Pet(name="Goldie",
                age=9,
                adopted = False,
                shelter = Shelter(name="Happy Animal Place"),
                breed = Breed(name="Golden Retriever", species=dog)
                #parent = spot
                )

    ginnie = Pet(name="Ginnie",
                age=1,
                adopted = False,
                shelter = goldie.shelter,
                breed = goldie.breed,
                parent = [goldie, spot]
                ) 
    
    blinkie = Pet(name="Blinkie",
                age=1,
                adopted = False,
                shelter = goldie.shelter,
                breed = Breed(name="Golden Dalmatian", species=dog),
                parent = [goldie, spot]
                )     


    log.info("Adding Goldie and Spot to session and committing changes to DB")
    db_session.add_all([spot, goldie, ginnie])
    db_session.commit()

    assert tom in spot.people
    spot.people.remove(tom)
    assert spot not in tom.pets

    #################################################
    #  Now it's up to you to complete this script ! #
    #################################################
    
    log.info("Creating breed trait items")
    fast = BreedTrait(name = "Fast")
    spotted = BreedTrait(name = "Spotted")
    gold = BreedTrait(name = "Gold")
    firedog = BreedTrait(name = "Fire dog")
    shorthair = BreedTrait(name = "Short Haired")
    longhair = BreedTrait(name = "Long Haired")
    
    log.info("Before adding traits to breed")
    breeds = db_session.query(Breed).all()
    for breed in breeds:
        print "Id: {}, Name: {}, pets: {}, traits: {}".format(breed.id, breed.name, \
            breed.pets, breed.traits)

    goldie.breed.traits.append(fast)
    goldie.breed.traits.append(gold)
    goldie.breed.traits.append(longhair)
    spot.breed.traits.append(fast)
    spot.breed.traits.append(spotted)
    spot.breed.traits.append(firedog)
    spot.breed.traits.append(shorthair)    
    goldie.person_associations.append(PetPersonAssociation (person=tom, nickname = "Bubbles"))
    #owner = spot.people  #also tried owner.id without success
    #spot.person_associations.append(PetPersonAssociation (person=owner, nickname = "Blacky"))
    spot.person_associations.append(PetPersonAssociation (person=sue, nickname = "Blacky"))
    
    log.info("Updating traits for breeds")
    db_session.add_all([goldie, spot])
    db_session.commit()   
    
    log.info("After adding traits to breed")
    breeds = db_session.query(Breed).all()
    for breed in breeds:
        print "Id: {}, Name: {}, pets: {}, traits: {}".format(breed.id, breed.name, \
            breed.pets, breed.traits)

    breedtraits = db_session.query(BreedTrait).all()
    for breedtrait in breedtraits:
        print "Id: {}, Name: {}".format(breedtrait.id, breedtrait.name)
    
    nicknames = db_session.query(PetPersonAssociation).all()
    for nickname in nicknames:
        print "Pet Name: {}, Person Name: {}, Nickname: {}, Child Name: {}".format(nickname.pet.name, nickname.person.full_name, nickname.nickname, nickname.pet.children)
    #################################################
    
    db_session.close()
    log.info("all done!")