from flask import Flask, render_template

app = Flask(__name__)

@app.route("/signup")
def index():
    return render_template("mizuki_signup.html")

app.run()
