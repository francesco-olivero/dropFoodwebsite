from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)


class Boxes(db.Model):
    __tablename__ = "boxes"
    id = db.Column(db.Integer, primary_key=True)
    boxName = db.Column(db.String(30), unique=True, nullable=False)
    labels = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)


class Ordini(db.Model):
    __tablename__ = "ordini"
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, primary_key=True)
    boxesIds = db.Column(db.String(100), nullable=False)  # boxes id separate by ", "
    boxesQtys = db.Column(db.String(100), nullable=False)  # boxes quantities separated by ", "
    totPrice = db.Column(db.Float, nullable=False)