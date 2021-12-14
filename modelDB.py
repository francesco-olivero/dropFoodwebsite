from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    '''def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_address(self):
        return self.address

    def get_role(self):
        return self.role'''


class Boxes(db.Model):
    __tablename__ = "boxes"
    id = db.Column(db.Integer, primary_key=True)
    boxName = db.Column(db.String(30), unique=True, nullable=False)
    labels = db.Column(db.String(100), nullable=False)
    foodOfferer = db.Column(db.Integer, db.ForeignKey('users.id'))  # foreignKey
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)  # per unit
    description = db.Column(db.String, nullable=True)

    def setQuantity(self, qty):
        self.quantity = int(qty)


class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))  # foreignKey
    totPrice = db.Column(db.Float, nullable=False)

    user = relationship("Users")


class OrderDetails(db.Model):
    __tablename__ = 'ordersDetails'
    id = db.Column(db.Integer, primary_key=True)
    boxId = db.Column(db.Integer, db.ForeignKey('boxes.id'))  # foreignKey
    orderId = db.Column(db.Integer, db.ForeignKey('orders.id'))  # foreignKey
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    order = relationship("Orders")
    boxes = relationship('Boxes')
