from  sqlalchemy.orm import sessionmaker
from darzelis_m2m import Produktas, Vaikas, Valgiarastis, Valgymas, produktu_suvartojimas, engine
from datetime import datetime

session = sessionmaker(bind=engine)()

def pasirinkimo_meniu():
    print("Sveiki atvykę, kokią operaciją norėsite atlikti?")
    print("1| Valdyti vaikų duomenis")
    print("2| Valdyti valgiarasčio informaciją")  
    print("3| Valdyti valgymų duomenis")
    print("4| Valdyti produktų duomenis")
    print("0| arba enter išeiti")
    return input("pasirinkite:") 

def vaiku_meniu():
    print("Vaikų duomenys")
    print("1| Įvesti vaiko duomenis")
    print("2| Peržiūrėti visus vaikų duomenis")  
    print("3| Peržiūrėti vaiko duomenis")
    print("4| Koreguoti duomenis")
    print("0| arba enter išeiti")
    return input("pasirinkite:") 

def valgiarastis_meniu():
    print("Valgiarasčio duomenys")
    print("1| Sukurti valgiaraštį")
    print("2| Peržiūrėti valgiarasčius")  
    print("3| Koreguoti valgiarasčius")
    print("0| arba enter išeiti")
    return input("pasirinkite:") 

def valgymu_meniu():
    print("Valgymų duomenys")
    print("1| Nurodyti suvalgymo būsena pagal vaiką")
    print("2| Peržiūrėti suvalgymo būsena")  
    print("3| Koreguoti")
    print("0| arba enter išeiti")
    return input("pasirinkite:") 

def produktu_meniu():
    print("Produktų duomenys")
    print("1| Įvesti produktus")
    print("2| Peržiūrėti produktus")  
    print("0| arba enter išeiti")
    return input("pasirinkite:") 

def add_vaikas():
    i_vardas = input("Įveskite vaiko vardą:")
    i_pavarde = input("Įveskite vaiko pavardę:")
    i_amzius = input("Įveskite vaiko amžių:")
    pridadamas_vaikas = Vaikas(vardas=i_vardas, pavarde=i_pavarde, amzius=i_amzius)
    session.add(pridadamas_vaikas)
    session.commit()

def preview_vaikai():
    vaikai = session.query(Vaikas).all()
    for vaikas in vaikai:
        print(f"ID: {vaikas.id}, Vardas: {vaikas.vardas}, Pavardė {vaikas.pavarde}, Amžius {vaikas.amzius}")

def preview_pagal_vaika():
    print("Visos vartotojo saskaitos: ")
    vaikai = session.query(Vaikas).filter_by(vardas=(input("Iveskite vaiko vardą: ")), pavarde=(input("Iveskite vaiko pavardę: "))).all()
    for vaikas in vaikai:
        print(f"ID: {vaikas.id}, Vardas: {vaikas.vardas}, Pavardė {vaikas.pavarde}, Amžius {vaikas.amzius}")

def get_vaikas_by_id():
    try:
        id = int(input("Vaikas ID: "))
    except ValueError:
        print("Error: ID turi būti skaičius")
    else:
        return session.query(Vaikas).get(id)

def update_vaikas(vaikas, **changes):
    for column, value in changes.items():
        if value:
            setattr(vaikas, column, value)
    session.commit()
    print(f"Vardas: {vaikas.vardas}, Pavardė {vaikas.pavarde}, Amžius {vaikas.amzius}")

def collect_changes(vaikas):
    print(f"Vardas: {vaikas.vardas}, Pavardė {vaikas.pavarde}, Amžius {vaikas.amzius}")
    print("Įveskite naują reikšmę arba palikite seną nieko neįvedant.")
    changes = {
        "vardas": input("Vardas: "),
        "pavarde": input("Pavardė: "),
        "amzius": input("Amžius: "),
    }
    return changes

def add_valgiarastis():
    i_savaites_diena = input("Įveskite savaitės dieną: ")
    i_tipas = input("Įveskite pasirinktinai, pusryčiai, pietūs, vakarienė: ")
    i_data = datetime.strptime(input("Įvekite datą METAI-MM-DD: "), "%Y-%m-%d")
    pridedamas_valgiarastis = Valgiarastis(savaites_diena=i_savaites_diena, tipas=i_tipas, data=i_data)
    session.add(pridedamas_valgiarastis)
    session.commit()

def preview_valgiarastis():
    valgiarasciai = session.query(Valgiarastis).all()
    for valgiarastis in valgiarasciai:
        print(f"ID: {valgiarastis.id}, Savaitės diena: {valgiarastis.savaites_diena}, Tipas: {valgiarastis.tipas}, Data: {valgiarastis.data}")

def get_valgiarastis_by_id():
    try:
        id = int(input("Valgiarastis ID: "))
    except ValueError:
        print("Error: ID turi būti skaičius")
    else:
        return session.query(Valgiarastis).get(id)

def update_valgiarastis(valgiarastis, **changes):
    for column, value in changes.items():
        if value:
            setattr(valgiarastis, column, value)
    session.commit()
    print(f"Savaitės diena: {valgiarastis.savaites_diena}, Valgiarasčio tipas {valgiarastis.tipas}, Data {valgiarastis.data}")

def collect_changes_valgiarastis(valgiarastis):
    print(f"Savaitės diena: {valgiarastis.savaites_diena}, Valgiarasčio tipas {valgiarastis.tipas}, Data {valgiarastis.data}")
    print("Įveskite naują reikšmę arba palikite seną nieko neįvedant.")
    changes = {
        "savaites_diena": input("Savaitės diena: "),
        "tipas": input("Valgiarasčio tipas: "),
        "data": input("Data: "),
    }
    return changes

def add_valgymas():
    i_suvalgymo_busena = input("Įveskite suvalgymų info nuo 0 iki 10, kai 0 nevalgė visai: ")
    i_vaikas_id = input("Įveskite norimo vaiko ID:  ")
    i_valgiarastis_id = input("Įveskite norimo valgiarasčio ID: ")
    pridedamas_valgiarastis = Valgymas(suvalgymo_busena=i_suvalgymo_busena, vaikas_id=i_vaikas_id, valgiarastis_id=i_valgiarastis_id)
    session.add(pridedamas_valgiarastis)
    session.commit()

def preview_valgymas():
    valgymai = session.query(Valgymas).all()
    for valgymas in valgymai:
        print(f"ID: {valgymas.id}, Suvalgymo būsena: {valgymas.suvalgymo_busena}, Vaikas ID: {valgymas.vaikas.id}, Valgiarastis ID: {valgymas.valgiarastis_id}")

def get_valgymas_by_id():
    try:
        id = int(input("Valgymas ID: "))
    except ValueError:
        print("Error: ID turi būti skaičius")
    else:
        return session.query(Valgymas).get(id)

def update_valgymas(valgymas, **changes):
    for column, value in changes.items():
        if value:
            setattr(valgymas, column, value)
    session.commit()
    print(f"ID: {valgymas.id}, Suvalgymo būsena: {valgymas.suvalgymo_busena}, Vaikas ID: {valgymas.vaikas.id}, Valgiarastis ID: {valgymas.valgiarastis_id}")

def collect_changes_valgymas(valgymas):
    print(f"ID: {valgymas.id}, Suvalgymo būsena: {valgymas.suvalgymo_busena}, Vaikas ID: {valgymas.vaikas.id}, Valgiarastis ID: {valgymas.valgiarastis_id}")
    print("Įveskite naują reikšmę arba palikite seną nieko neįvedant.")
    changes = {
        "suvalgymo_busena": input("Suvalgymo būsena: "),
        "vaikas_id": input("Vaikas_id: "),
        "valgiarastis_id": input("Valgiaraštis_id: "),
    }
    return changes

def add_produktas(valgiarastis=None):
    i_pavadinimas = input("Įveskite produktą: ")
    i_kaina = input("Įveskite kainą: ")
    i_produktas = Produktas(pavadinimas=i_pavadinimas, kaina=i_kaina)
    if valgiarastis:
        i_produktas.valgiarasciai.append(valgiarastis)
    session.add(i_produktas)
    session.commit()

def preview_produktai():
    produktai = session.query(Produktas).all()
    for produktas in produktai:
        print(f"ID: {produktas.id}, Pavadinimas: {produktas.pavadinimas}, Kaina: {produktas.kaina}")

while True:
    choice = pasirinkimo_meniu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        choice1 = vaiku_meniu()
        if choice1 == "0" or choice1 == "":
            break
        elif choice1 == "1":
            add_vaikas()
        elif choice1 == "2":
            preview_vaikai()
        elif choice1 == "3":
            preview_pagal_vaika() 
        elif choice1 == "4":
            vaikas = get_vaikas_by_id()
            update_vaikas(vaikas, **collect_changes(vaikas))      

    elif choice == "2":
        choice2 = valgiarastis_meniu()
        if choice2 == "0" or choice2 == "":
            break
        elif choice2 == "1":
            add_valgiarastis()
        elif choice2 == "2":
            preview_valgiarastis()
        elif choice2 == "3":
            valgiarastis = get_valgiarastis_by_id()
            update_valgiarastis(valgiarastis, **collect_changes_valgiarastis(valgiarastis))   

    elif choice == "3":
        choice3 = valgymu_meniu()
        if choice3 == "0" or choice3 == "":
            break
        elif choice3 == "1": 
            add_valgymas()
        elif choice3 == "2": 
            preview_valgymas()
        elif choice3 == "3":
            valgymas = get_valgymas_by_id()
            update_valgymas(valgymas, **collect_changes_valgymas(valgymas))

    elif choice == "4":
        choice4 = produktu_meniu()
        if choice4 == "0" or choice4 == "":
            break
        elif choice4 == "1":
            add_produktas()
        elif choice4 == "2":
            preview_produktai()


# def preview_pagal_vaika():
#     print("Visos vartotojo saskaitos: ")
#     vaikas = session.query(Vaikas).filter_by(vardas=(input("Iveskite vaiko vardą: ")), pavarde=(input("Iveskite vaiko pavardę: "))).all()
#     for vaikas_valgymas in vaikas.valgymai:
#         print(f"ID: {vaikas_valgymas.suvalgymo_busena}, ID: {vaikas_valgymas.id}")

# def add_produktas():
#     i_valgiarastis_id = int(input("Įveskite norimo pildyti valgiarasčio ID: "))
#     i_pavadinimas = input("Įveskite produktą: ")
#     i_kaina = input("Įveskite kainą: ")
#     i_produktas = Produktas(pavadinimas=i_pavadinimas, kaina=i_kaina, valgiarasciai=i_valgiarastis_id)
#     session.add(i_produktas)
#     session.commit()