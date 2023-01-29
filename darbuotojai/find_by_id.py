import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
    print("Atskyrimas kableliais, nieko kad iseiti")
    paieska = input("Iveskite ID: ")
    if paieska == "":
        break
    else:
        ids = paieska.split(',')
        with conn:
            #c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
            query = "SELECT * FROM darbuotojai WHERE rowid IN (" + ','.join(['?' for _ in range(len(ids))]) + ")"
            print(query)
            c.execute(query, ids)
            while True:
                darbuotojas = c.fetchone() #istraukti duomenis atskirose eilutese
                if darbuotojas:
                    print(darbuotojas) #spausdina duomenis rezultata
                else:
                    print("...daugiau nieko nera")
                    break

                #_ zemas bruksnys siukslinis kintamas kai jo reikia, bet nenaudojame
                #rowid jei duomenu baze neturi id stulpelio pats squelite ji sukuria