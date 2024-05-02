from flask import Flask, render_template, request, redirect, session
from db import Database

app = Flask(__name__)
db = Database('db.db')

app.secret_key = 's3cr3t' # lol, +1 vulnerability

@app.route('/', methods=['GET'])
def index():
    noaccess = request.args.get('noaccess') is not None
    return render_template('index.html', noaccess=noaccess), 200 if not noaccess else 403

@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    is_valid = db.check_credentials(login, password)
    if is_valid:
        session['has_access'] = True
        return redirect('/panel')
    else:
        session['has_access'] = False
        return redirect('/?noaccess')

@app.route('/panel', methods=['GET', 'POST'])
def panel():
    if session['has_access']:
        return render_template('panel.html')
    else:
        return redirect('/?noaccess')

if __name__ == '__main__':
    app.run()