# Animals
# ID | Name | Habitat

# Zookeeper Log
# ID | Animal ID (Foreign Key) | Notes
from sqlalchemy import (create_engine, Column, Integer,
                        String, ForeignKey,select)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine("sqlite:///zoo.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    habitat = Column(String)
    logs = relationship("Logbook", back_populates="animal",
                        cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"""
    \nAnimal {self.id}\r
    Name = {self.name}\r
    Habitat = {self.habitat}
    """


class Logbook(Base):
    __tablename__ = "logbook"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    notes = Column(String)
    animal = relationship("Animal", back_populates="logs")

    def __repr__(self):
        return f"""
    \nLogbook {self.id}\r
    Animal ID = {self.animal_id}\r
    Notes = {self.notes}
    """
def CreateAnimal(name):
    habitat=input('Where does it live? ')
    new_animal=Animal(name=name,habitat=habitat)
    session.add(new_animal)
    session.commit()

    if session.dirty: #check to see if database changed at all
        print(session.dirty)

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    animal_list_query=session.query(Animal.name).all()
    Animal_list=[]
    for tup in animal_list_query:
        for value in tup:
            Animal_list.append(value)
    print(Animal_list)
    animal_check=input("Enter a new animal or choose from list above ")
    if animal_check in Animal_list:
        current_animal = session.query(Animal).filter_by(name=animal_check).first()
        print(current_animal)
    else:
        CreateAnimal(name=animal_check)

