from flask import render_template, request, redirect, url_for, session, flash, Response, jsonify
from flask import Flask
from forms import *
from database.database import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import auth, config
import os

# # from From import MyForm
app = Flask(__name__, template_folder='Templates',instance_relative_config=True)
# app.config['SECRET_KEY'] = 'project'

app.secret_key = 'project'

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'database.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# app.config.from_pyfile('config.py')
app.debug = True


db = SQLAlchemy(app)

config.init_app(app)
app.register_blueprint(auth.bp)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/properties')
def properties():
    return render_template('properties.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        # elif db.execute(
        #         'SELECT id FROM user WHERE username = ?', (username,)
        # ).fetchone() is not None:
        #     error = 'User {} is already registered.'.format(username)

        # if error is None:
        #     db.execute(
        #         'INSERT INTO user (username, password) VALUES (?, ?)',
        #         (username, generate_password_hash(password))
        #     )
        #     db.commit()
            return redirect(url_for('login'))
        flash(error)
        # 模拟验证
        if username == 'admin' and password == '123': #buyer
            session['name'] = username
            return render_template('BuyerMainPage.html')
        if username == 'admin2' and password == '123':  #seller
            session['name'] = username
            return render_template('SellerMainPage.html')
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
                'SELECT id FROM account WHERE username = ?', (username,)
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

    return render_template('register.html')

@app.route('/registerAsBuyer', methods=['GET', 'POST'])
def registerAsBuyer():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        print(email)
        print(username)
        print(password)
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('login'))

        flash(error)
    # if username == 'admin' and password == '123':
    #     session['name'] = username
    #     return redirect(url_for('register'))
    # if username != 'admin':
    #     flash('no this name')
    return render_template('registerAsBuyer.html')

@app.route('/registerAsSeller', methods=['GET', 'POST'])
def registerAsSeller():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        print(email)
        print(username)
        print(password)
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('login'))

        flash(error)
        # if username == 'admin' and password == '123':
        #     session['name'] = username
        #     return redirect(url_for('register'))
        # if username != 'admin':
        #     flash('no this name')
        return render_template('registerAsSeller.html')





if __name__ == '__main__':

    app.run()
    # db.create_all()

