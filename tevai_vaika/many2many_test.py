from  sqlalchemy.orm import sessionmaker
from many2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

# kestutis = Tevas(vardas="Kestutis", pavarde="Januskevicius")
# emilija = Vaikas(vardas="Emilija", pavarde="Januskevicius")
# kestutis.vaikai.append(emilija)
# session.add(kestutis)
# session.commit()

# mama = Tevas(vardas="Nicoletta", pavarde="Januskeviciene")
# emilija = session.query(Vaikas).filter_by(vardas="Emilija").one()
# if emilija:
#     mama.vaikai.append(emilija)
# session.add(mama)
# session.commit()

tetis_ir_mama = session.query(Tevas).filter(Tevas.pavarde.ilike("Janus%")).all()
tetis_ir_mama[0].pavarde = "Januskevicius"
tetis_ir_mama[1].pavarde = "Januskeviciene"
# maja= Vaikas(vardas="Maja", pavarde= "Januskeviciute", tevai=tevai)
# session.commit()

marco = Vaikas(vardas="Marco", pavarde="Januskevicius", tevai=tetis_ir_mama) #tevai kintamasis is Vaikai klase, tetis_ir_mama yra ivestieji tevai
session.add(marco)
session.commit()

