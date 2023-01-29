import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/programa.db')
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__ = 'Darbuotojų duomenų bazė'
    id = Column(Integer, primary_key = True)
    name = Column('vardas', String)
    last_name = Column('pavarde', String)
    birthdate = Column("gimimo data", DateTime)
    position = Column('pareigos', String)
    salary = Column('atlyginimas', Float)
    works_since = Column('dirba nuo', DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, last_name, birthdate, position, salary):
        self.name = name
        self.last_name = last_name
        self.birthdate = birthdate
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"({self.name}, {self.last_name}, {self.birthdate}, {self.position}, {self.salary}, {self.works_since})"

    def __str__(self) :
        return f"ID {self.id}, Vardas: {self.name}, Pavarde: {self.last_name}, Gimimo data: {self.birthdate}, Pareigos: {self.position}, Atlyginimas: {self.salary}, Dirba nuo: {self.works_since}"

if __name__ == '__main__':
    Base.metadata.create_all(engine)