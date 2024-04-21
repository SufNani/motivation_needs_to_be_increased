from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    conn = sqlite3.connect('sampledb.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sample WHERE id = 1')
    row = cursor.fetchall()[0]
    conn.close()
    context = {
        "id": 0,
        "login": "admin",
        "password": "admin",
        "name": row[1],
        "surname": "Adminsov",
        "age": row[2],
        "balance": 1000000
    }
    return render_template("index.html", **context)

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

app.run()
