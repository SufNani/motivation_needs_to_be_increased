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
    print(cur.execute('SELECT name FROM adepts').fetchall())
    context = {
        "adepts": [
            {
                "name": cur.execute('SELECT name FROM adepts').fetchall()[i][0],
                "points": cur.execute('SELECT points FROM adepts').fetchall()[i][0]
                } for i in range(cur.execute('SELECT COUNT(*) FROM adepts').fetchall()[0][0])
            ]
        }
    cur.close()
    conn.close()

    return render_template('Dmitry_Table.html', **context)

@app.route("/shop")
def shop():
    conn = sqlite3.connect('static/db/dmitry_shop.db')
    cur = conn.cursor()
    print(cur.execute('SELECT image_src FROM cards').fetchall())
    context = {
        "cards": [
            {
                "image_src": cur.execute("SELECT image_src FROM cards").fetchall()[i][0],
                "price": cur.execute("SELECT price FROM cards").fetchall()[i][0],
                "title": cur.execute("SELECT title FROM cards").fetchall()[i][0],
                "description": cur.execute("SELECT description FROM cards").fetchall()[i][0]
            } for i in range(cur.execute('SELECT COUNT(*) FROM cards').fetchall()[0][0])
        ]
    }

    return render_template("Dmitry_Shop.html", **context)
app.run()
