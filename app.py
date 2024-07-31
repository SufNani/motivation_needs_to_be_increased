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
        cursor.execute("SELECT name, phone_number, email, birthday, living_place FROM user WHERE id = ?",
                       (session['user_id'],))
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
            return render_template('user.html', **context)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        email = request.form.get('email')
        password = request.form.get('password')
        cursor.execute(
            "SELECT id, name, phone_number, email, birthday, living_place, password FROM user WHERE email = ?",
            (email,))
        user = cursor.fetchone()
        conn.close()

        if user is None:
            return '<h1>User with this email not found</h1>'
        elif user[6] != password:
            return redirect('/login')
        else:
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            return redirect('/user')
    return render_template('login.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    rules_has_error = False
    password_unmatch = False
    if request.method == "POST":
        rules = request.form.get("rules")
        password = request.form.get("password")
        r_password = request.form.get("re-password")
        email = request.form.get("email")
        name = request.form.get("name")

        if not rules:
            rules_has_error = True
        elif password != r_password:
            password_unmatch = True
        else:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO user(name, email, password) VALUES (?, ?, ?)", (name, email, password))
                conn.commit()
            except sqlite3.IntegrityError as e:
                # handle the error if needed, e.g., email already exists
                return f"<h1>An error occurred: {e}</h1>"
            finally:
                conn.close()
            return redirect('/login')

    return render_template('signup.html', rules_has_error=rules_has_error, password_unmatch=password_unmatch)


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))




@app.route("/table")
def table():
    if 'user_id' in session:
        conn = database.Database('database.db')
        context = {"adepts": conn.select('name, points', 'dmitry_table_adepts')}
        conn.kill()
        return render_template('Dmitry_Table.html', **context)
    return redirect(url_for('login'))


@app.route("/shop")
def shop():
    if 'user_id' in session:
        # conn = database.Database('database.db')
        # context = {
        #     "cards": conn.select('image_src, price, title, description', 'dmitry_shop_cards')
        # }
        # conn.kill()
        return render_template("shop.html")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()

