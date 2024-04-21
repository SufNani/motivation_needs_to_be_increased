from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    context = {
        "city": "tomsk",
        "user": [
            {
                "name": "mark",
                "balance": 1488,
                "account_age": 0,
            }
        ]

    }
    return render_template("index.html")

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

@app.route('/admin')
def admin():
    return render_template('mark_admin.html')

@app.route('/user')
def user():
    conn = sqlite3.connect('static/sqlite.db')
    cursor = conn.cursor()
    cursor.execute('select * from sample where id = 1')
    row = cursor.fetchall()[0]
    conn.close()
    context = {
        "user": {
            "name" : row[1],
            "phone_number": row[2],
            "email": row[4],
            "birthday": row[3],
            "living_place": row[5]
        }
    }
    for row in row:
        print(row)
    return render_template('mark_user.html', **context)

@app.route('/login')
def login():
    return render_template('mark_login.html')

app.run()