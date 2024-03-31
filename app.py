from flask import Flask, render_template

app = Flask(__name__)

@app.route("/table")
def table():
	return render_template("Dmitry_Table.html")

@app.route('/')
def shop():
	return render_template("Dmitry_Shop.html")

app.run()