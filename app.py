import datetime
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, balance, birthday FROM user WHERE id = 1')
    row = cursor.fetchall()[0]
    conn.close()
    context = {
        "user": {
            "balance": row[1],
            "name": row[0],
            "birthday": row[2],
            "year": datetime.datetime.now().year,
            "email": "info@rubius.com",
            "phone_number": "+7-(3822)-9-7777-2"
        }
    }
    return render_template("sasha_menu.html", **context)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    rules_has_error = False
    print(request.method)
    if request.method == "POST":
        rules = request.form.get("rules")
        password = request.form.get("password")
        r_password = request.form.get("repeated_password")
        email = request.form.get("email")
        name = request.form.get("name")
        if rules != "on":
            rules_has_error = True
        else:
            conn = sqlite3.connect("ITOG.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO user(login, email, password) VALUES (?, ?, ?)", (name, email, password))
            return render_template("mark_user.html")
    print(rules_has_error)
    return render_template("mizuki_signup.html", rules_has_error=rules_has_error)


@app.route('/admin')
def admin():
    return render_template('mark_admin.html')


@app.route('/user')
def user():
    user_id = request.args.get('id')
    password = request.args.get('password')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone_number,email,birthday,living_place FROM user ")
    row = cursor.fetchall()[0]
    conn.close()
    context = {
        "user": {
            "phone_number": row[1],
            "email": row[2],
            "birthday": row[3],
            "living_place": row[4]
        }
    }
    return render_template('mark_user.html', **context)


@app.route('/login',methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        email = request.form.get('email')
        password = request.form.get('password')
        cursor.execute("SELECT name, phone_number,email, birthday, living_place, password FROM user where email = ?",(email,))
        user = cursor.fetchone()
        conn.close()

        if user is None:
            return '<h1>юзер с такой почтой не найден</h1>'
        elif user[5] != request.form.get('pass'):
            return "нет"
        else:
            return "да"
    else:
        return render_template('mark_login.html', error=error)


@app.route("/table")
def table():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    print(cur.execute('SELECT name FROM dmitry_table_adepts').fetchall())
    context = {
        "adepts": [
            {
                "name": cur.execute('SELECT name FROM dmitry_table_adepts').fetchall()[i][0],
                "points": cur.execute('SELECT points FROM dmitry_table_adepts').fetchall()[i][0]
                } for i in range(cur.execute('SELECT COUNT(*) FROM dmitry_table_adepts').fetchall()[0][0])
            ]
        }
    cur.close()
    conn.close()
    return render_template('Dmitry_Table.html', **context)


@app.route("/shop")
def shop():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    print(cur.execute('SELECT image_src FROM dmitry_shop_cards').fetchall())
    context = {
        "cards": [
            {
                "image_src": cur.execute("SELECT image_src FROM dmitry_shop_cards").fetchall()[i][0],
                "price": cur.execute("SELECT price FROM dmitry_shop_cards").fetchall()[i][0],
                "title": cur.execute("SELECT title FROM dmitry_shop_cards").fetchall()[i][0],
                "description": cur.execute("SELECT description FROM dmitry_shop_cards").fetchall()[i][0]
            } for i in range(cur.execute('SELECT COUNT(*) FROM dmitry_shop_cards').fetchall()[0][0])
        ]
    }
    return render_template("Dmitry_Shop.html", **context)


app.run()