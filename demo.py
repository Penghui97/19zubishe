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
        if username == 'admin' and password == '123':
            session['name'] = username
            return redirect(url_for('register'))
        if username != 'admin':
            flash('no this name')
    return render_template('login.html')
    # # 从数据库中验证信息
    # form=LoginForm()
    # account=Account.query.all()
    # if form.validate_on_sumbit():
    #     if  account.email==form.email.data and account.username==form.username.data and account.password==form.password.data:
    #         db.session.commit()




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
        # 提交信息到数据库中
        # form=RegisterForm()
        # account=Account(email,username,password)
        # db.session.add(account)
        # db.session.commit()
        # flash('Your information is saved.')
    return render_template('register.html')


'''
@app.route('/buyer_interface',method=['GET','POST'])
def show_house():
    form=HouseForm()  # 现在还没有创建HouseForm表单
    if request.method=='POST' or form.validate_on_submit():
        db.session.add()
        '''




if __name__ == '__main__':

    app.run()
    # db.create_all()

