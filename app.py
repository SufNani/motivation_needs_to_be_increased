from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/admin')
def admin():
    return render_template('mark_admin.html')
@app.route('/user')
def user():
    return render_template('mark_user.html')
@app.route('/login')
def login():
    return render_template('mark_login.html')

