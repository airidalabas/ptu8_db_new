from  sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

kestutis = Tevas(vardas="Kestutis", pavarde="Januskevicius")
emilija = Vaikas(vardas="Emilija", pavarde="Januskeviciute")
maja = Vaikas(vardas="Maja", pavarde="Januskeviciute")
marco = Vaikas(vardas="Marco", pavarde="Januskevicius")

#pirmas varinatas
kestutis.vaikai.append(emilija)
kestutis.vaikai.append(maja)
kestutis.vaikai.append(marco)
session.add(kestutis)
session.commit()

#alternatyvus jeigu nera kitu vaiku
# kestutis.vaikai = [emilija, maja, marco]
# session.add(kestutis)
# session.commit()

# marco.tevas = kestutis
# maja.tevas = kestutis
# emilija.tevas = kestutis
# session.add(marco)
# session.add(emilija)
# session.add(maja)
# session.commit()