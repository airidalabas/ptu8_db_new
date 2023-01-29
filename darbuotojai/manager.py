import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
    print("Iveskite nieko, kad iseiti")
    paieska = input("Ko ieskome?: ")
    if paieska == "":
        break
    else:
        paieska = f"%{paieska}%" #i imputa paduoda %
        with conn:
            #c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
            c.execute("SELECT * FROM darbuotojai WHERE pavarde LIKE ? OR vardas LIKE ?", (paieska, paieska))
            while True:
                darbuotojas = c.fetchone() #istraukti duomenis atskirose eilutese
                if darbuotojas:
                    print(darbuotojas) #spausdina duomenis rezultata
                else:
                    print("...daugiau nieko nera")
                    break

# 'OR 1=1 -- taip is paieskos galima istraukti visus duomenis, todel reikia apsaugoti paieska