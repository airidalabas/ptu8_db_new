import sqlite3
import os

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('data/automobiliai.db')
with conn:
    c = conn.cursor()
    c.execute(""" 
     CREATE TABLE IF NOT EXISTS automobiliai (
            id INTEGER PRIMARY KEY NOT NULL,
            gamintojas VARCHAR(50) NOT NULL,
            modelis VARCHAR(10) NOT NULL,
            metai INTEGER NOT NULL,
            spalva VARCHAR(50) NOT NULL,
            kaina FLOAT
        )
    """)

#c.execute("INSERT INTO automobiliai (gamintojas, modelis, spalva, metai, kaina) VALUES ('GMC', 'Sierra', 5555.55);")   