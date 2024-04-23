import sqlite3

connection = sqlite3.connect('bal.db')
cursor = connection.cursor()

login = 'Sasha'
balance = '1488'


cursor.execute('INSERT INTO bal (balance, login) '
               'VALUES (?, ?)', (balance, login))

cursor.execute('SELECT * FROM bal')
user = cursor.fetchall()
print(user)