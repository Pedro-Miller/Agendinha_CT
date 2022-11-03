import sqlite3

db = sqlite3.connect('database.sqlite')
cursor = db.cursor()

limpador = int(input("Digite 10 para apagar tudo e 500 para selecionar um nome\n"))

if limpador<100:
    cursor.execute("DELETE FROM contas where dre < 99999999999999")
else:
    limpanome = input("qual o nome\n")
    cursor.execute("DELETE FROM contas where nome  = '"+limpanome+"'")
                     
db.commit()



