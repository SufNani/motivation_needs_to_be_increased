from flask import Flask, render_template
<<<<<<< HEAD
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("../templates/loginSasha.html")
=======

app = Flask(__name__)

@app.route("/table")
def table():
	return render_template("Dmitry_Table.html")

@app.route('/shop')
def shop():
	return render_template("Dmitry_Shop.html")
>>>>>>> Dmitry

app.run()