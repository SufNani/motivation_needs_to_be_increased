import datetime

from flask import Flask, render_template

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
@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

@app.route("/signup")
def signup():
    return render_template("mizuki_signup.html")

app.run()
