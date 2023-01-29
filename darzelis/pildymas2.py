def preview_pagal_vaika():
    print("Visos vartotojo saskaitos: ")
    vaikas = session.query(Vaikas).filter_by(vardas=(input("Iveskite vaiko vardą: ")), pavarde=(input("Iveskite vaiko pavardę: "))).all()
    for vaikas_valgymas in vaikas.valgymai:
        print(f"ID: {vaikas_valgymas.suvalgymo_busena}, ID: {vaikas_valgymas.id}")

def add_produktas():
    i_valgiarastis_id = int(input("Įveskite norimo pildyti valgiarasčio ID: "))
    i_pavadinimas = input("Įveskite produktą: ")
    i_kaina = input("Įveskite kainą: ")
    i_produktas = Produktas(pavadinimas=i_pavadinimas, kaina=i_kaina, valgiarasciai=i_valgiarastis_id)
    session.add(i_produktas)
    session.commit()