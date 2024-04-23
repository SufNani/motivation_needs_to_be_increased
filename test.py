import sqlite3

connection = sqlite3.connect('bal.db')
cursor = connection.cursor()

login = 'sasha'
balance = '1488'


#cursor.execute('INSERT INTO bal (balance, login) '
#               'VALUES (?, ?)', (balance, login))


try:
    cursor.execute('SELECT * from bal where login? and balance =?', (login,balance))
    Balance = cursor.fetchall()


#cursor.execute('SELECT * FROM bal')
#user = cursor.fetchall()
#print(user)