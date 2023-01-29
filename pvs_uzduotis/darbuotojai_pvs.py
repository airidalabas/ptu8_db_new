from modelis import Darbuotojai, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

session = sessionmaker(bind=engine)()

def choice_menu():
    print("---Darbuotojų duomenų bazė---")
    print("1 | įvesti darbuotojo duomenis ")
    print("2 | peržiurėti darbuotojo duomenis ")
    print("3 | redaguoti darbuotojo duomenis ")
    print("4 | ištrinti darbuotojo duomenis ")
    print("0 | iseiti")
    choice = input("Pasirinkite norimą veiksmą: ")
    return choice

def add_darbuotojas():
    name = input("vardas: ")
    last_name = input("pavarde: " )
    birthdate = datetime.strptime(input("gimimo data METAI-MM-DD: "), "%Y-%m-%d")
    position = input("pareigos: ")
    salary = float(input("atlyginimas: "))
    darbuotojai = Darbuotojai(name, last_name, birthdate, position, salary)
    session.add(darbuotojai)
    session.commit()
    print(darbuotojai)
    return darbuotojai

def look_darbuotojai():
    all = session.query(Darbuotojai).all()
    if all:
        for darbuotojai in all:
            print(darbuotojai)
    else:
        print("Darbuotojai nerasti")

# def look_darbuotojai(query=session.query(Darbuotojai)):
#     if query and len(query.all()) > 0:
#         for darbuotojas in query.all():
#             print(darbuotojas)
    
def update_darbuotojai():
    try:
        id = int(input("Įveskite darbuotojo ID: "))
    except ValueError:
        print("darbuotojo ID turi buti skaicius.")
    else:
        darbuotojas = session.query(Darbuotojai).get(id)
        try:
            #if not ivedimas1 == "": si salyga taip pat grazina klaida ir pereina prie kito veiksmo)
            #if ivedimas:(jeigu reiksme tuscias stringas if salyga grazins false ir pereis prie kito veiksmo)
            ivedimas1 = input("Įveskite vardą:")
            if ivedimas1: 
                darbuotojas.name = ivedimas1
            ivedimas2 = input("Įveskite pavardę:")
            if ivedimas2:
                darbuotojas.last_name = ivedimas2 
            ivedimas3 = input("Įveskite gimimo datą METAI-MM-DD: ")
            if ivedimas3:
                darbuotojas.birthdate = datetime.strptime(ivedimas3, "%Y-%m-%d")
            ivedimas4 = input("Įveskite pareigas: ")
            if ivedimas4:
                darbuotojas.position = ivedimas4
            ivedimas5 = input("Įveskite atlyginimą: ")
            if ivedimas5:
                darbuotojas.salary = float(ivedimas5)
        except:
            print("Įvyko klaida, bandykite iš naujo")
        else:
            session.commit()
            print(f"Darbuotojas {darbuotojas} atnaujintas sėkmingai.")

def dalete_darbuotojas():
    try:
        trinimas = int(input("Su kuriuo id norite trinti darbuotoja?"))
    except ValueError:
        print("Id turi buti skaicius")
    istrintas = session.query(Darbuotojai).get(trinimas)
    session.delete(istrintas)
    session.commit()
    print(f"Darbuotojas {istrintas} sekmingai istrintas")

while True:
    choice = choice_menu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        add_darbuotojas()
    elif choice == "2":
        look_darbuotojai()
    elif choice == "3":
        look_darbuotojai()
        update_darbuotojai()
    elif choice == "4":
        look_darbuotojai()
        dalete_darbuotojas()



