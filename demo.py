from flask import render_template, request, redirect, url_for, session, flash, Response, jsonify
from flask import Flask
from forms import *
from database.database import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import auth, config
import os
import re
import pandas as pd

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

@app.route('/property-single',methods=['GET','POST'])
def property_single():
    img_path=request.cookies.get('imagine')
    house_name=request.cookies.get('house_name')
    house_price=request.cookies.get('house_price')
    house_location = request.cookies.get('house_location')
    str_house_name=re.sub("%20"," ",str(house_name))
    str_house_price = re.sub("%24", "$", str(house_price))
    str_house_price=re.sub("%2C",",",str_house_price)
    str_house_location = re.sub("%2C", ",", str(house_location))
    str_house_location = re.sub("%20", " ", str_house_location)
    return render_template('property-single.html',img1=img_path,house_name=str_house_name,house_location=str_house_location,house_price=str_house_price)

@app.route('/BuyerNewHouse',endpoint='BuyerNewHouse',methods=['GET','POST'])
def BuyerNewHouse():
    if request.method=='POST':
        return redirect(url_for('property-single'))
    return render_template('BuyerNewHouse.html')


@app.route('/BuyerSecondHand')
def BuyerSecondHand():
    return render_template('BuyerSecondHand.html')

@app.route('/BuyerRent')
def BuyerRent():
    return render_template('BuyerRent.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/BuyerProfile')
def BuyerProfile():
    return render_template('BuyerProfile.html')

@app.route('/SellerProfile')
def SellerProfile():
    return render_template('SellerProfile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        db = config.get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            session['name'] = username
            return render_template('BuyerMainPage.html')

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
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     print(email)
    #     print(username)
    #     print(password)
    #     db = config.get_db()
    #     error = None
    #
    #     if not username:
    #         error = 'Username is required.'
    #     elif not password:
    #         error = 'Password is required.'
    #     elif not email:
    #         error = 'Email is required.'
    #     elif db.execute(
    #             'SELECT id FROM account WHERE username = ?', (username,)
    #     ).fetchone() is not None:
    #         error = 'User {} is already registered.'.format(username)
    #
    #     if error is None:
    #         db.execute(
    #             'INSERT INTO account (username, password, email) VALUES (?, ?, ?)',
    #             (username, generate_password_hash(password), email)
    #         )
    #         db.commit()
    #         return redirect(url_for('login'))

        # flash(error)

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
        db = config.get_db()
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
                'INSERT INTO user (username, password,email) VALUES (?, ?, ?)',
                (username, generate_password_hash(password), email)
            )
            db.commit()
            return redirect(url_for('login'))
        else:
            flash(error)
    # return redirect(url_for('registerAsBuyer'))
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
                'INSERT INTO user (username, password, email) VALUES (?, ?, ?)',
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
        return render_template('registerAsSeller.html')


@app.route('/prediction')
def prediction_of_price():
    pattern = re.compile(r'\d+')
    data = pd.read_csv('bj.csv', encoding='gb18030')

    cnt = 0
    for row in data['单价/平']:
        try:
            data.loc[cnt, '单价/平'] = pattern.findall(data.loc[cnt, '单价/平'])
            int(row)
        except ValueError:
            pass
        cnt += 1

    data['单价/平'] = data['单价/平'].astype('int')

    df_total_price = data.loc[data.index[0:len(data)], ['城区', '房价']]
    df_permeter_price = data.loc[data.index[0:len(data)], ['城区', '单价/平']]

    series1 = df_total_price.groupby('城区')['房价'].mean()
    series2 = df_permeter_price.groupby('城区')['单价/平'].mean()

    series = pd.concat([series1, series2], axis=1)

    districts = []
    average_total_price = []
    average_permeter_price = []

    for item in series1.index:
        districts.append(item)
    for item in series1.values:
        average_total_price.append(item * 10000)
    for item in series2.values:
        average_permeter_price.append(item)

    context = {'districts': districts, 'average_total_price': average_total_price,'average_permeter_price': average_permeter_price}

    return render_template('Prediction.html',**context)


if __name__ == '__main__':
    app.run()
    #db.create_all()


