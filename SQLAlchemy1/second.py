from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "Species: %s" % self.name

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)