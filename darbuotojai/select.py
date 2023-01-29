import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

with conn:
    c.execute("UPDATE darbuotojai SET vardas='Sandra', pavarde='Krisiunaite' WHERE id = 3;")
    c.execute("DELETE FROM darbuotojai WHERE id = 4;")


    c.execute("SELECT * FROM darbuotojai;") #c yra kaip kursorius, execute ivykdo uzklausa bet rezultato dar nera
    #darbuotojai = c.fetchall() #atiduoti, sukelti, istraukti duomenis visus eilute
    while True:
        darbuotojas = c.fetchone() #istraukti duomenis atskirose eilutese
        if darbuotojas:
            print(darbuotojas) #spausdina duomenis rezultata
        else:
            break



#if darbuotojai:
 #   print(darbuotojai)