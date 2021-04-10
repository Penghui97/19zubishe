from flask import render_template, request, redirect, url_for, session, flash, Response, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import config
import auth
import os

# # from From import MyForm
app = Flask(__name__, template_folder='Templates',instance_relative_config=True)
# app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'database.db'),
#     )
app.secret_key = 'project'
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'database.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# app.config.from_pyfile('config.py')
app.debug = True

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = MyForm()
    # if form.validate_on_submit():  # 将会检查是否是一个 POST 请求并且请求是否有效。
    #     return redirect(url_for(''))  # 如有有效就重定向到首页
    # name = request.form.get('name')
    # password = request.form.get('password')
    # print(name)
    # return render_template('rendering.html', form=form)
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    if username == 'admin' and password == '123':
        session['name'] = username
        return redirect(url_for('login'))
    if username != 'admin':
        flash('no this name')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        print(email)
        print(username)
        print(password)
        db = config.get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required.'
        elif db.execute(
                'SELECT id FROM account WHERE username = ?',(username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO account (username, password, email) VALUES (?, ?, ?)',
                (username, generate_password_hash(password), email)
            )
            db.commit()
            return redirect(url_for('login'))

        flash(error)
    # if username == 'admin' and password == '123':
    #     session['name'] = username
    #     return redirect(url_for('register'))
    # if username != 'admin':
    #     flash('no this name')
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
    db.create_all()

