from  sqlalchemy.orm import sessionmaker
from bankai_m2m import Bankas, Asmuo, Saskaita, engine

session = sessionmaker(bind=engine)()

def pasirinkimo_meniu():
    print("Sveiki atvykę į savo banką, kokią operaciją norėsite atlikti?")
    print("1| įveskiti vartotoją")
    print("2| įvesti banką")  
    print("3| įvesti saskaitą")
    print("4| įvesti pajamas/išlaidas")   
    print("5| peržiūrėti vartotojus") 
    print("6| peržiūrėti bankus")       
    print("7| peržiūrėti visas sąskaitas") 
    print("8| peržiūrėti sąskaitas pagal vartotojo ID")     
    print("0| išeiti")
    return input("pasirinkite:") 

def ivesti_asmuo():
    i_vardas = input("iveskite varda: ")   
    i_pavarde = input('iveskite pavarde: ')    
    i_asmens_kodas = input("iveskite asmens koda: ")  
    i_tel_nr =  input("ivekite telefono numeri: ")
    pridedamas_asmuo = Asmuo(vardas=i_vardas, pavarde=i_pavarde, asmens_kodas=i_asmens_kodas, tel_nr=i_tel_nr)
    session.add(pridedamas_asmuo)
    session.commit()
    print("____vartotojas sekmingai ivestas____")

def perziureti_vartotojus():
    asmenys = session.query(Asmuo).all()
    for asmuo in asmenys:
        #print(asmuo) tada reikia pagrindiniame lange suskurti str
        print(asmuo.id, asmuo.vardas, asmuo.pavarde, asmuo.asmens_kodas, asmuo.tel_nr)

def ivesti_banka():
    i_pavadinimas = input("iveskite banko pavadinima: ")
    i_adresas = input("iveskite banko adresa: ")
    i_banko_kodas = input("iveskite banko koda: ")
    i_swift = input("iveskite banko swift: ")
    pridedamas_bankas = Bankas(pavadinimas=i_pavadinimas, adresas=i_adresas, banko_kodas=i_banko_kodas, swift=i_swift)
    session.add(pridedamas_bankas)
    session.commit()
    print("____bankas sekmingai ivestas____")

def perziureti_bankus():
    bankai = session.query(Bankas).all()
    for bankas in bankai:
        print(bankas.id, bankas.pavadinimas, bankas.adresas, bankas.banko_kodas, bankas.swift)

def ivesti_saskaita():
    i_numeris =input("iveskite saskaitos nr: ")
    i_balansas = input("iveskite saskaitos balansa: ")
    nauja_saskaita = Saskaita(numeris=i_numeris, balansas=i_balansas)
    asmuo = session.query(Asmuo).get(int(input("iveskite asmens ID: ")))
    asmuo.saskaitos.append(nauja_saskaita)
    bankas = session.query(Bankas).get(int(input("Iveskite banko ID: ")))
    bankas.saskaitos.append(nauja_saskaita)
    session.add(nauja_saskaita)
    session.commit()

def pajamos():
    asmuo = session.query(Asmuo).get(int(input("Nurodykite asmens id su kurio saskaita atliksite veiksmus: ")))
    if len(asmuo.saskaitos) > 0:
        for saskaita in asmuo.saskaitos:
            print(saskaita.id, saskaita.numeris, saskaita.balansas, saskaita.bankas.pavadinimas)
        saskaita = session.query(Saskaita).get(int(input("Nurodykite saskaitos id su kuria atliksite veiksmus: ")))
        pajamos = float(input("iveskite pajamas arba islaidas su -(minusu): "))
        saskaita.balansas += pajamos
        session.commit()
        print(f"Atnaujintas balansas: {saskaita.balansas}")
    else:
        ("Asmuo saskaitos neturi")
        

def perziureti_saskaitas():
    print("Visos saskaitos: ")
    saskaitos = session.query(Saskaita).all()
    for saskaita in saskaitos:
        print(f"Saskatos id: {saskaita.id}, Saskaitos nr: {saskaita.numeris}, Balansas: {saskaita.balansas}")

# def perziureti_sask_pagal_asmeni():
#     print("Visos vartotojo saskaitos: ")
#     asmuo = session.query(Asmuo).get(int(input("Iveskite id asmens, kurio saskaitas noresite perziureti")))
#     for asmuo_saskaita in asmuo.saskaitos:
#         print(f"Vartotojo saskaitos{asmuo_saskaita.numeris}")

def perziureti_sask_pagal_asmeni():
    print("Visos vartotojo saskaitos: ")
    asmuo = session.query(Asmuo).filter_by(id=int(input("Iveskite id asmens, kurio saskaitas noresite perziureti"))).one()
    for asmuo_saskaita in asmuo.saskaitos:
        print(f"Vartotojo saskaitos: {asmuo_saskaita.numeris}")

while True:
    choice = pasirinkimo_meniu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        ivesti_asmuo()
    elif choice == "2":
        ivesti_banka()
    elif choice == "3":
        ivesti_saskaita()
    elif choice == "4":
        perziureti_vartotojus()
        pajamos()
    elif choice == "5":
        perziureti_vartotojus()
    elif choice == "6":
        perziureti_bankus()    
    elif choice == "7":
        perziureti_saskaitas()
    elif choice == "8":
        perziureti_sask_pagal_asmeni()
   