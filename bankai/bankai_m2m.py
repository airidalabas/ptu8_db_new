from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/bankai_m2m.db')
Base = declarative_base()


class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key = True)
    pavadinimas = Column(String)
    adresas = Column(String)
    banko_kodas = Column(Integer)
    swift = Column(String)
    saskaitos = relationship("Saskaita", back_populates="bankas")
   
class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key = True)
    vardas = Column(String)
    pavarde = Column(String)
    asmens_kodas = Column(Integer)
    tel_nr = Column(Integer)
    saskaitos = relationship("Saskaita", back_populates="asmuo")
                                                                                                                                                                                                                                           

class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key = True)
    numeris = Column(String)
    balansas = Column(Float)
    bankas_id = Column('bankas_id', Integer, ForeignKey('bankas.id'))
    bankas = relationship("Bankas", back_populates="saskaitos")
    asmuo_id = Column('asmuo_id', Integer, ForeignKey('asmuo.id'))
    asmuo = relationship("Asmuo", back_populates="saskaitos")


if __name__ == "__main__":
    Base.metadata.create_all(engine)