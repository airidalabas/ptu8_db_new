from sqlalchemy import create_engine #sujingimas su duomenu baze
from sqlalchemy.orm import sessionmaker
from model import Project

engine = create_engine('sqlite:///data/projektai.db')
#Session = sessionmaker(bind=engine)
#session = Session()
session = sessionmaker(bind=engine)()

# CRUD = create read update delete
# Create susikuriame irasus
# naujas_projektas = Project("Brangus Reikalai", 14000)
# kitas_prjektas = Project("Geras puslapiukas", 500)
# session.add(naujas_projektas)
# session.add(kitas_prjektas)
# session.commit()

#Read/ SELECT ieskome irasu
# projektas1 = session.query(Project).get(1)
# print(projektas1)

# projektas1 = session.query(Project).get(2)  #per query nusirodome is kokios klases paduoda info
# projektas2 = session.query(Project).filter_by(name="Kiti reikalai").one() #issifitravome antraja uzklausa
#print(projektas2)
# projektai = session.query(Project).all()
# print(projektai)

#pigus_projektai = session.query(Project).filter(Project.price<=10000).all()
#print(pigus_projektai)

reikalai = session.query(Project).filter(Project.name.ilike("%reikala%")).all() #keys insetintive
print(reikalai)

#update /pakeiciame projekto kaina is 14000 i 100000
# brangus = session.query(Project).filter(Project.price > 10000, Project.name.ilike("%brangus%")).first()
# brangus.price = 100000
# session.commit()
# print(brangus)

#delete
# projektas2 = session.query(Project).filter_by(name="Kiti reikalai").one()
# session.delete(projektas2)
# session.commit()
# projektai = session.query(Project).all()
# print(projektai)
