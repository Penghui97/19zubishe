
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__, template_folder='Templates')

app.config['SECRET_KEY'] = 'project'
app.secret_key = 'project'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    if name == 'admin' and password == '123':
        session['name'] = name
        return redirect(url_for('login'))
    if name != 'admin':
        flash('no this name')
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
