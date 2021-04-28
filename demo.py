from flask import render_template, request, redirect, url_for, session, flash, Response, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from . import auth
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

db.init_app(app)
app.register_blueprint(auth.bp)


@app.route('/')
def hello_world():
    return render_template('index.html')


<<<<<<< Updated upstream
=======
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

@app.route('/SellerMainPage')
def sellfer_main_page():
    if request.method=='POST':
        redirect(url_for('NewHouse'))
    return render_template('SellerMainPage.html')

@app.route('/BuyerMainPage')
def buyer_main_page():

    if request.method=='POST':
        redirect(url_for('NewHouse.html'))

    return render_template('BuyerMainPage.html')


# BuyerMainPage指向的界面的视图函数
@app.route('/BuyerNewHouse',endpoint='BuyerNewHouse')
def buyer_new_house():
    return render_template('BuyerNewHouse.html')

@app.route('/BuyerSecondHand',endpoint='BuyerSecondHand')
def buyer_second_hands():
    return render_template('BuyerSecondHand.html')

@app.route('/BuyerRent',endpoint='BuyerRent')
def buyer_rent_house():
    return render_template('BuyerRentHouse.html')

@app.route('/BuyerOrderLists',endpoint='BuyerOrderLists')
def buyer_order_lists():
    return render_template('BuyerOrderLists.html')

@app.route('/BuyerOperationProcess',endpoint='BuyerOperationProcess')
def buyer_operation_process():
    return render_template('BuyerOperationProcess.html')

@app.route('/BuyerPredictionOfPrice',endpoint='BuyerPredictionOfPrice')
def buyer_prediction_of_price():
    return render_template('BuyerPredictionOfPrice.html')


# SellerMainPage指向的界面的视图函数
@app.route('/SellerNewHouse',endpoint='SellerNewHouse')
def buyer_new_house():
    return render_template('BuyerNewHouse.html')

@app.route('/SellerSecondHand',endpoint='SellerSecondHand')
def buyer_second_hands():
    return render_template('BuyerSecondHand.html')

@app.route('/SellerRent',endpoint='SellerRent')
def buyer_rent_house():
    return render_template('BuyerRentHouse.html')

@app.route('/SellerOrderLists',endpoint='SellerOrderLists')
def buyer_order_lists():
    return render_template('SellerOrderLists.html')

@app.route('/SellerOperationProcess',endpoint='SellerOperationProcess')
def buyer_operation_process():
    return render_template('BuyerOperationProcess.html')

@app.route('/SellerPredictionOfPrice',endpoint='SellerPredictionOfPrice')
def buyer_prediction_of_price():
    return render_template('SellerPredictionOfPrice.html')


>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            error = 'User {} is already registered.'.format(username)
=======
            session['name'] = username
            return render_template('BuyerMainPage.html')

        # if error is None:
        #     db.execute(
        #         'INSERT INTO user (username, password) VALUES (?, ?)',
        #         (username, generate_password_hash(password))
        #     )
        #     db.commit()
        #    return redirect(url_for('login'))
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



>>>>>>> Stashed changes

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
    db.create_all()



