from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('mark_user.html')

app.run()
