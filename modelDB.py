from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    userBoxes = db.relationship('Box', backref='offerer')  # 1 to many
    userOrders = db.relationship('Order', backref='user')  # 1 to many


class Box(db.Model):
    __tablename__ = "boxes"
    id = db.Column(db.Integer, primary_key=True)
    boxName = db.Column(db.String(30), unique=True, nullable=False)
    labels = db.Column(db.String(100), nullable=False)
    foodOfferer = db.Column(db.Integer, db.ForeignKey('users.id'))  # foreignKey
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)  # per unit
    description = db.Column(db.String, nullable=True)

    contenuto = db.relationship('OrderDetails', backref='box')  # 1 to many

    def setQuantity(self, qty):
        self.quantity = int(qty)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))  # foreignKey
    totPrice = db.Column(db.Float, nullable=False)

    con = db.relationship('OrderDetails', backref='order')  # 1 to many


class OrderDetails(db.Model):
    __tablename__ = 'ordersDetails'
    id = db.Column(db.Integer, primary_key=True)
    boxId = db.Column(db.Integer, db.ForeignKey('boxes.id'))  # foreignKey
    orderId = db.Column(db.Integer, db.ForeignKey('orders.id'))  # foreignKey
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
