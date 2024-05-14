import datetime
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    context = {
        "year": datetime.datetime.now().year,
        "email": "info@rubius.com",
        "phone_number": "+7-(3822)-9-7777-2",
    }
    return render_template("index.html")
<<<<<<< Updated upstream


@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"
=======
>>>>>>> Stashed changes

@app.route('/user')
def user():
    user_id = request.args.get('id')
    password = request.args.get('password')
    return f'User ID: {user_id}, Password: {password}'

@app.route("/signup", methods=["GET", "POST"])
def signup():
<<<<<<< Updated upstream
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
=======
    
    return render_template("mizuki_signup.html")
>>>>>>> Stashed changes

app.run()
