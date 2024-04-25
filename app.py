from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    context = {
        "id": 0,
        "login": "admin",
        "password": "admin",
        "name": "Adminus",
        "surname": "Adminsov",
        "age": 0,
        "balance": 1000000
    }
    return render_template("index.html", **context)

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

@app.route("/table")
def table():
    conn = sqlite3.connect('static/db/dmitry_table.db')
    cur = conn.cursor()
    context = {
        "adepts": [
            {
                "name": cur.execute('SELECT name FROM adepts').fetchall()[0][i],
                "points": cur.execute('SELECT points FROM adepts').fetchall()[0][i]
                } for i in range(cur.execute('SELECT COUNT(*) FROM adepts').fetchall()[0][0])
            ]
        }
    return render_template('Dmitry_Table.html', **context)

app.run()
