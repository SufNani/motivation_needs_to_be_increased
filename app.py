from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    context = {
        "id": 0,
        "login": "admin",
        "password": "admin",
        "name": "Adminus",
        "surname": "Adminsov",
        "age": 0,
        "balance": 1000000
    }
    return render_template("index.html", **context)

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

app.run()
