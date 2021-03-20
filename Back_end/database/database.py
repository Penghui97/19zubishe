from Back_end import db

class Account(db.Model):
    userID=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String,index=True,unique=True)
    password=db.Column(db.String,index=True)
    identity=db.Column(db.String)

class Client(db.Model):
    clientID=db.Column(db.Integer,primary_key=True)
    client_permission = db.Column(db.String, index=True)
    buyerID=db.Column(db.Integer,db.ForeignKey('buyer.ID'))   # client 指向 buyer 的外键
    sellerID=db.Column(db.Integer,db.ForeignKey('seller.ID'))   # client 纸箱 seller 的外键


class Admin(db.Model):
    adminID=db.Column(db.Integer,primary_key=True)
    admin_permission=db.Column(db.String,index=True)


class Buyer(db.Moder):
    ID=db.Column(db.Integer,primary_key=True)
    state=db.Column(db.String)
    ID_card_number=db.Column(db.String,index=True,unique=True)
    phone_number=db.Column(db.String,index=True,unique=True)
    order_numbers=db.Column(db.Integer)
    order_id=db.Column(db.Integer,db.ForeignKey('order.ID'))   # buyer 指向 order 的外键


class Seller(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    state=db.Column(db.String)
    ID_card_number=db.Column(db.String,index=True,unique=True)
    phone_number = db.Column(db.String, index=True, unique=True)
    order_numbers = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.ID'))    # seller 指向 order 的外键


class Order(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.String)
    house_ID=db.Column(db.Integer,db.ForeignKey('house.ID'))
    buyers=db.relationship('Buyer')
    sellers=db.relationship('Seller')

class House(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.String)
    price=db.Column(db.Float,index=True)
    area = db.Column(db.Float, index=True)
    location=db.Column(db.String)
    state=db.Column(db.String)
    orders=db.relationship('Order')
