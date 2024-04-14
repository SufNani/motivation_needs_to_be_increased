from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    time = datetime.datetime.now()
    context = {
        "time": f"{time.day}.0{time.month}.{time.year}",
        "user": {
            "balance": 1488
        }
    }
    return render_template("sasha_menu.html", **context)

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

@app.route("/menu")
def signup():
    return render_template("sasha_menu.html")

app.run()
