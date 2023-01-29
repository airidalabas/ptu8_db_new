import sqlite3
import os

if not os.path.exists('data'): #pasitikriname ar yra duomenu katalogas jei nera susikuriame
    os.mkdir('data')

conn = sqlite3.connect('data/darbuotojai.db') #galima susikurti ir tuscia duomenu baze data/tuscia
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS darbuotojai (
            id INTEGER PRIMARY KEY NOT NULL,
            vardas VARCHAR(50) NOT NULL,
            pavarde VARCHAR(100) NOT NULL,
            atlyginimas DECIMAL(10,2)
        )
    """)


    c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Giedrius', 'Isora', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Airida', 'Juraitiene', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Egle', 'Motiejunaite', 777.77);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Daiva', 'Mamama', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Kestuti', 'Bauzys', 5555.55);")

    darbuotojai = [
        ('Egidijus', 'Jankunas', 0),
        ('Gediminas', 'Zakas', 10033.71),
        ('Iganas', 'Rocys', 6789.10),
        ('Kevinas', 'Karpus', 69849.65),
    ]
    c.executemany("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES (?, ?, ?)", darbuotojai)

