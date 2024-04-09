from flask import Flask, render_template

app = Flask(__name__)

@app.route("/shop")
def index():
    return render_template("Dmitry_Shop.html")

@app.route("/table")
def test():
    return render_template("Dmitry_Table.html")

app.run()
