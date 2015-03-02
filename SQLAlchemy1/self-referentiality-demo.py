from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import logging


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


class Amoeba(Base):
    __tablename__ = 'amoeba'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)    

    # foreign key to self, must be nullable, as some pets will be the roots of our trees!
    parent_id = Column(Integer, ForeignKey('amoeba.id'), nullable=True ) 
    # Many-to-One relationship
    parent = relationship('Amoeba', remote_side='Amoeba.id', backref="children" )

    def __repr__(self):
        return self.name


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
    engine = create_engine('sqlite:///:memory:')
    # if we asked to init the db from the command line, do so
    if True:
        init_db(engine)
    # call the sessionmaker factory to make a Session class 
    Session = sessionmaker(bind=engine)
    # get a local session for the this script
    db_session = Session()
    log.info("Session created: {}".format(db_session) )
   

    # create parents and children
    root = Amoeba(name='Root')
    child_1 = Amoeba(name='Left Half Child', parent=root)
    child_2 = Amoeba(name='Right Half Child', parent=root)
    grandchild_1 = Amoeba(name='Left  1', parent=child_1)

    family = [root, child_1, child_2, grandchild_1]
    for member in family:
        parent = member.parent
        log.info("{}'s parent is {}".format(member.name, parent if parent else "none because it's root!" ))

    log.info('You can get to root from grandchild by following parents...')
    assert grandchild_1.parent.parent == root
    
    db_session.add_all([grandchild_1, child_1])

    db_session.commit()

    import pdb
    pdb.set_trace()

    db_session.close()
    log.info("all done!")