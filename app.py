from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/test")
def test():
    return render_template("mark.admin.html")
@app.route("/test1")
def test1():
    return render_template("mark.user.html")
@app.route("/test2")
def test2():
    return render_template("mark.login.html")