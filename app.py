from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    context = {
        "city": "tomsk",
        "user": [
            {
                "name": "mark",
                "balance": 1488,
                "account_age": 0,
            }
        ]

    }
    return render_template("index.html")

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

@app.route('/admin')
def admin():
    return render_template('mark_admin.html')

@app.route('/user')
def user():
    context = {
        "user": {
            "phone_number": "1111",
            "email": "aaa@gmail.com",
            "birthday": "01.01.1900",
            "living_place": "Пушкина 1"
        }

    }
    return render_template('mark_user.html', **context)

@app.route('/login')
def login():
    return render_template('mark_login.html')

app.run()