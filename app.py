import datetime
import database

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    conn = database.Database('database.db')
    context = conn.select('name, balance, birthday', 'user', uslovie = 'id = 1')
    conn.kill()
    context = {"user": database.json_merge(context, {
        "year": datetime.datetime.now().year,
        "email": "info@rubius.com",
        "phone_number": "+7-(3822)-9-7777-2"
    })}
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
    conn = database.Database('database.db')
    context = {"user": conn.select("name, phone_number, email,birthday, living_place", "user")}
    conn.kill()
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
    conn = database.Database('database.db')

    context = {"adepts": conn.select('name, points', 'dmitry_table_adepts')}
    conn.kill()
    return render_template('Dmitry_Table.html', **context)

@app.route("/shop")
def shop():
    conn = database.Database('database.db')
    context = {"cards": conn.select('image_src, price, title, description', 'dmitry_shop_cards')}
    conn.kill()
    return render_template("Dmitry_Shop.html", **context)


app.run()
