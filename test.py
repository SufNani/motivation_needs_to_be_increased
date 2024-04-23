import sqlite3

connection = sqlite3.connect('sql.db')
cursor = connection.cursor()

name = 'Sasha'
login = 'vasya'


cursor.execute('INSERT INTO User (name, login) '
               'VALUES (?, ?)', (name, login))

cursor.execute('SELECT * FROM User')
user = cursor.fetchall()
print(user)