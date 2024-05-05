from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3
@app.route('/')
def index():
    conn = sqlite3.connect('static/ITOG.db')
    cursor = conn.cursor()
    cursor.execute('select * from user')
    row = cursor.fetchall()[0]

    conn.close
    return render_template('index.html')
@app.route('/admin')
def admin():
    return render_template('mark_admin.html')
@app.route('/user')
def user():
    conn = sqlite3.connect('static/ITOG.db')
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
@app.route('/login')
def login():
    return render_template('mark_login.html')

@app.route("/signup")
def signup():
    email = request.args.get('email')
    print(email)
    return render_template('mizuki_signup.html')
app.run()

