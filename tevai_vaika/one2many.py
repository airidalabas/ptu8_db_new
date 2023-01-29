from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data/tevai_vaikai_o2m.db')
Base = declarative_base()

class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key = True)
    vardas = Column(String)
    pavarde = Column(String)
    vaikai = relationship("Vaikas", back_populates="tevas")

class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    makymo_istaiga = Column(String)
    tevas_id = Column(Integer, ForeignKey("tevas.id")) #tevas yra foreinkey is vaikai (tevas yra tevo lenteles pavadinimas, o id is tevo lenteleje ir tevas.id ir tevas_id sutampa tik yra skirtingose lentelese tevas_id yra vaiko lentele)
    tevas = relationship("Tevas", back_populates="vaikai") #vaikai kryziuojasi su kintamuoju per back_populates, o klase Tevas turi buti didzioji raide



if __name__ == "__main__":
    Base.metadata.create_all(engine)