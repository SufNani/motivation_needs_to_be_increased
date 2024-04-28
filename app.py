from flask import Flask, render_template
import sqlite3

app = Flask(__name__)




@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    conn = sqlite3.connect('ITOG.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, balance, birthday FROM user WHERE id = 1')
    row = cursor.fetchall()[0]
    conn.close()
    context = {
        "user": {
            "balance": row[1],
            "name": row[0],
            "birthday": row[2]
        }
    }
    return render_template("sasha_menu.html", **context)

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

@app.route("/menu")
def signup():
    return render_template("sasha_menu.html")

app.run()
