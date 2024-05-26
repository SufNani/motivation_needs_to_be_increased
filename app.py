from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3, database, datetime

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
    return render_template("index.html", **context)



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
                    "name": row[0],
                    "phone_number": row[1],
                    "email": row[2],
                    "birthday": row[3],
                    "living_place": row[4]
                }
            }
            return render_template('new_user.html', **context)
    return redirect(url_for('login'))


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
            return redirect('/login')
        else:
            return redirect('/user')
    return render_template('new_login.html')


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
            conn.commit()
            conn.close()
            return redirect('/user')
    print(rules_has_error)
    return render_template('new_signup.html', rules_has_error=rules_has_error)
@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))




@app.route("/table")
def table():
    conn = database.Database('database.db')
    context = {"adepts": conn.select('name, points', 'dmitry_table_adepts')}
    conn.kill()
    return render_template('Dmitry_Table.html', **context)

@app.route("/shop")
def shop():
    conn = database.Database('database.db')
    context = {
        "cards": conn.select('image_src, price, title, description', 'dmitry_shop_cards')
    }
    conn.kill()
    return render_template("Dmitry_Shop.html", **context)

@app.route('/menu')
def menu():
    return render_template('sasha_menu.html')

if __name__ == '__main__':
    app.run()

