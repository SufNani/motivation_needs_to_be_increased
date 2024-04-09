from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/main")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return "<h1>Это тестовая страница!!!</h1>"

@app.route("/shop")
def shop():
    return render_template("Dmitry_Shop.html")

@app.route("/table")
def table():
    return render_template("Dmitry_Table.html")

app.run()
