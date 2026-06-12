import sqlite3
conn=sqlite3.connect('bazakoktela.db')
print("Baza otvorena uspesno")

conn.execute(''' CREATE TABLE IF NOT EXISTS kokteli (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ime TEXT,
                sastojci TEXT,
                jacina TEXT,
                ukus TEXT                
)''')
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Mojito", "Rum", "Blago", "Slatko"))
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Daiquiri", "Rum", "Srednje", "Kiselo"))
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Margarita", "Tequila", "Srednje", "Kiselo"))
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Cosmopolitan", "Votka, Liker", "Srednje", "Slatko"))
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Martini", "Gin, Votka", "Jako", "Gorko"))
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Pina Colada", "Rum, Liker", "Blago", "Slatko"))
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Negroni", "Gin", "Jako", "Gorko"))
conn.execute("INSERT INTO kokteli (ime, sastojci, jacina, ukus) VALUES (?, ?, ?, ?)", ("Sex on the Beach", "Votka, Liker", "Blago", "Slatko"))
conn.commit()
conn.close()
print("Baza kreirana")