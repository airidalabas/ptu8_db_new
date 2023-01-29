from  sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

tevas = session.query(Tevas).filter(Tevas.vardas == "Kestutis").first()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

print('vaiko tevas')
marco = session.query(Vaikas).filter(Vaikas.vardas == "Marco").first()
print(marco.vardas, 'tevas yra', marco.tevas.vardas)

print ("vaiko tevo antras vaikas")
print(marco.tevas.vaikai[1].vardas)

print ("vaiko tevo antras vaikas") #antras vairantas
bauble = marco.tevas.vaikai[1]
print(bauble.vardas)

print ("vaiko tevo antras vardas pakoreguota pavarde")
#saraso elementas neturi jokios sasajos su ID
bauble = marco.tevas.vaikai[1]
print(bauble.vardas)
bauble.pavarde = "Baublyte"
session.commit()
print(bauble.vardas, bauble.pavarde)

emilija = tevas.vaikai[0]
if emilija.vardas == "Emilija":
    tevas.vaikai.remove(emilija)
else:
    print("Emilija jau ir yra", emilija.vardas)
session.commit()

