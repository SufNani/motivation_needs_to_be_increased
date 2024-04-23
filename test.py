import sqlite3
conn = sqlite3.connect('static/sqlite.db')
cursor = conn.cursor()
def populate_db(name,phone_number,birthday,email,living_place):
    cursor.execute('INSERT INTO sample(name,phone_number,birthday,email,living_place) VALUES(?,?,?,?,?)', (10000,12,'01.01.01','aaa','aa'))
    conn.commit()
populate_db(100,11,'01.01.01','aaa@email.com','aa,1')
cursor.execute('SELECT * from sample')
rows = cursor.fetchall()
for row in rows:
    print(row)