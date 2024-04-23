import sqlite3
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()
def populate_db():
    cursor.execute('INSERT INTO balance(name, balance) VALUES(?,?)', ('sasha', 1000))
    conn.commit()

populate_db(1488, 1000)

cursor.execute('SELECT * from sample')
rows = cursor.fetchall()
for row in rows:
    print(row)