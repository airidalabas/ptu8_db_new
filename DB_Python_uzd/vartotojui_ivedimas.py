import sqlite3

conn = sqlite3.connect("data/automobiliai.db")
c = conn.cursor()

while True:
    pasirinkimas = int(input("Sveiki, kokį veiksmą norite atlikti: veiksmas IVESTI spauskite 1 ar SURASTI spauskite 2?: "))
    if pasirinkimas == 1:
        e_gamintojas = input("Automobilio gamintojas: ")
        e_modelis = input("Automobilio modelis: ")
        e_metai = input("Automobilio metai: ")
        e_spalva = input("Automobilio spalva: ")
        e_kaina = input("Automobilio kaina: ")

        c.execute("INSERT INTO automobiliai (gamintojas, modelis, metai, spalva, kaina ) VALUES (?, ?, ?, ?, ?)", (e_gamintojas, e_modelis, e_metai, e_spalva, e_kaina))
        conn.commit()
        print("Duomenys sėkmingai įvesti")

    if pasirinkimas == 2:
        p_gamintojas = input("Kokio automobilio ieskote? : ")
        p_modelis = input("Kokio auto modelio ieskote? : ")
        p_metai = range(int(input("Nuo kokiu metu automobilio ieskote? Jei norite pradeti nuo saraso pradzios veskite 0: ")),int(input("Iki kokiu metu automobilio ieskote: ")))
        p_spalva = input("Kokios spalvos automobilio ieskote? : ")
        p_kaina = range(int(input("Nuo kokios kainos automobilio ieskote? Jei norite pradeti nuo saraso pradzios veskite 0: ")),int(input("Iki kokios kainos automobilio ieskote: ")))
        p_gamintojas = f"%{p_gamintojas}%"
        p_modelis = f"%{p_modelis}%"
        p_metai = f"%{p_metai}%"
        p_spalva = f"%{p_modelis}%"
        p_kaina = f"%{p_kaina}%"

        with conn:
            c.execute("SELECT * FROM automobiliai WHERE gamintojas LIKE ? AND modelis LIKE ? AND metai LIKE ? AND spalva LIKE ? AND kaina LIKE ? ", (p_gamintojas, p_modelis, p_metai, p_spalva, p_kaina)) 
            while True:
                automobilis = c.fetchone()
                if (automobilis):
                    print(automobilis)
                else:
                    print("viskas")
                    break

    if pasirinkimas == "":
        break

