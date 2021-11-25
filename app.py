from flask import Flask
from flask import render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'utenti.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

from modelDB import User

@app.before_first_request
def create_db():
    db.drop_all()
    db.create_all()
    jack = User(username='jack', email='jack000@example.com')
    fra = User(username='fra', email='fra@example.com')
    db.session.add(jack)
    db.session.add(fra)
    db.session.commit()

@app.route('/')
def main_page():
    # users = User.query.all()
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/carrello')
def carrello():
    return render_template("carrello.html")

@app.route('/collabora')
def collabora():
    return render_template("collabora.html")

if __name__ == '__main__':
    app.run()
    # appFlask.run(debug=True)
