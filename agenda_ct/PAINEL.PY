import sqlite3

def cria_agenda_porra():
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS agenda ([evento] TEXT NOT NULL,[descrição] TEXT NOT NULL,[dia] TEXT NOT NULL, [mes] TEXT NOT NULL);''')
    
    db.commit()
        
cria_agenda_porra()

