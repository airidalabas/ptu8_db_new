from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/tevai_vaikai_m2m.db')
Base = declarative_base()

tevai_vaikai = Table("tevas_vaikas", Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('tevas_id', Integer, ForeignKey('tevas.id')),
    Column('vaikas_id', Integer, ForeignKey('vaikas.id')),
)

class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key = True)
    vardas = Column(String)
    pavarde = Column(String)
    vaikai = relationship("Vaikas", secondary=tevai_vaikai, back_populates="tevai") #secondary tarpine lentele
   

class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    makymo_istaiga = Column(String)
    tevai = relationship("Tevas", secondary=tevai_vaikai, back_populates="vaikai")
    


if __name__ == "__main__":
    Base.metadata.create_all(engine)