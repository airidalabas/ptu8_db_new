import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/darzelis_m2m.db')
Base = declarative_base()

class Vaikas(Base):
    __tablename__= "vaikas"
    id = Column(Integer, primary_key = True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    amzius = Column("Amžius", Integer)
    valgymai = relationship("Valgymas", back_populates="vaikas")

def __str__(self):
        return f"ID: {self.id}, Vaiko vardas: {self.vardas}, Vaiko pavardė {self.pavarde}, Amžius {self.amzius}"


class Valgymas(Base):
    __tablename__ = "valgymas"
    id = Column(Integer, primary_key = True)
    suvalgymo_busena = Column("Suvalgymo būsena", Integer)
    vaikas_id = Column("Vaikas_id", Integer, ForeignKey('vaikas.id'))
    valgiarastis_id = Column("Valgiaraštis_id", Integer, ForeignKey("valgiarastis.id"))
    vaikas = relationship("Vaikas", back_populates = "valgymai")
    valgiarastis = relationship("Valgiarastis", back_populates = "valgymai" )

def __str__(self):
        return f"ID: {self.id}, Suvalgymo būsena: {self.suvalgymo_busena}, Vaikas ID: {self.vaikas.id}, Valgiarastis ID: {self.valgiarastis_id}"


produktu_suvartojimas = Table("produktu_suvartojimas", Base.metadata,
    Column("id", Integer, primary_key = True),
    Column("valgiarastis_id", Integer, ForeignKey("valgiarastis.id")),
    Column("produktas_id", Integer, ForeignKey("produktas.id")),
)

class Valgiarastis(Base):
    __tablename__ = "valgiarastis"
    id = Column(Integer, primary_key = True)
    savaites_diena = Column("Savaitės diena", String)
    tipas = Column("Dienos valgymai", String)
    data = Column("Data", DateTime, default = datetime.datetime.utcnow)
    valgymai = relationship("Valgymas", back_populates = "valgiarastis")
    produktai = relationship("Produktas", secondary = produktu_suvartojimas, back_populates = "valgiarasciai")

def __str__(self) :
        return f"ID: {self.id}, Savaitės diena: {self.savaites_diena}, Tipas: {self.tipas}, Data: {self.data}"

class Produktas(Base):
    __tablename__= "produktas"
    id = Column(Integer, primary_key = True)
    pavadinimas = Column("Pavadinimas", String)
    kaina = Column("Kaina", Integer)
    valgiarasciai = relationship("Valgiarastis", secondary = produktu_suvartojimas, back_populates = "produktai")

def __str__(self):
    return f"ID: {self.id}, Pavadinimas: {self.pavadinimas}, Kaina: {self.kaina}"

if __name__ == '__main__':
    Base.metadata.create_all(engine)