from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key


@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    user = None
    if 'user_id' in session:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, balance, birthday FROM user WHERE id = ?', (session['user_id'],))
        row = cursor.fetchone()
        conn.close()
        if row:
            user = {
                "balance": row[1],
                "name": row[0],
                "birthday": row[2]
            }
    context = {"user": user}
    return render_template("sasha_menu.html", **context)


@app.route('/admin')
def admin():
    if 'user_id' in session:
        return render_template('mark_admin.html')
    return redirect(url_for('login'))


@app.route('/user')
def user():
    if 'user_id' in session:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone_number, email, birthday, living_place FROM user WHERE id = ?", (session['user_id'],))
        row = cursor.fetchone()
        conn.close()
        if row:
            context = {
                "user": {
                    "phone_number": row[1],
                    "email": row[2],
                    "birthday": row[3],
                    "living_place": row[4]
                }
            }
            return render_template('mark_user.html', **context)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        email = request.form.get('email')
        password = request.form.get('password')
        cursor.execute("SELECT id, name, phone_number, email, birthday, living_place, password FROM user WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user is None:
            error = 'User with this email not found'
        elif user[6] != password:
            error = 'Incorrect password'
        else:
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            return redirect(url_for('index'))
    return render_template('mark_login.html', error=error)


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
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO user(login, email, password) VALUES (?, ?, ?)", (name, email, password))
            return render_template("mark_user.html")
    print(rules_has_error)
    return render_template("mizuki_signup.html", rules_has_error=rules_has_error)


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))


@app.route("/table")
def table():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT name, points FROM dmitry_table_adepts')
    adepts = cur.fetchall()
    context = {
        "adepts": [{"name": adept[0], "points": adept[1]} for adept in adepts]
    }
    cur.close()
    conn.close()
    return render_template('Dmitry_Table.html', **context)


@app.route("/shop")
def shop():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT image_src, price, title, description FROM dmitry_shop_cards')
    cards = cur.fetchall()
    context = {
        "cards": [{"image_src": card[0], "price": card[1], "title": card[2], "description": card[3]} for card in cards]
    }
    cur.close()
    conn.close()
    return render_template("Dmitry_Shop.html", **context)


@app.route("/menu")
def menu():
    return render_template("sasha_menu.html")


if __name__ == '__main__':
    app.run()