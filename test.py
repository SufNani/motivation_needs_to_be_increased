import sqlite3


conn = sqlite3.connect('sampledb.db')
cursor = conn.cursor()


def populate_db(name, balance):
    cursor.execute('INSERT INTO sample(name, balance) VALUES (?, ?)', (name, balance))
    conn.commit()

populate_db('asd', 155)


cursor.execute('SELECT * from sample')
rows= cursor.fetchall()
for row in rows:
    print(row)

