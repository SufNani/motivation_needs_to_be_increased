import sqlite3
conn = sqlite3.connect('static/sql.db')
cursor = conn.cursor()
#def populate_db(name,phone_number,birthday,email,living_place):
#cursor.execute('INSERT INTO User(name,phone_number,birthday,email,living_place) '
 #        'VALUES(?,?,?,?,?)', (10000,12,'01.01.01','aaa','aa'))
#conn.commit()
#populate_db('a',11,'01.01.01','aaa@email.com','aa,1')
login = input('login')
password = input('password')
try:
    cursor.execute('SELECT * from User where login=? and password =?', (login,password))
    User = cursor.fetchall()
    if User:
      print(f'вы успешно вошли {login}')
      print(f'ваша дата рождения{User}')

except:
    print(User)
#cursor.execute('SELECT * from User')
#rows = cursor.fetchall()
#print(rows)
