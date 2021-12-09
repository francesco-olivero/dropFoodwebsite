from flask import Flask, redirect, flash, session, request
from flask import render_template, url_for
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dropFood.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'hard to guess'
db = SQLAlchemy(app)

from modelDB import User, Boxes, Ordini
from form import RegisterForm, LoginForm


@app.before_first_request
def create_db():
    # db.drop_all()
    db.create_all()
    # admin = User(username='admin', email='a@example.com', password='pass', first_name='aaa', last_name='nnn', birthday=19990430, phone=3343445980, role='gestore')
    # db.session.add(admin)
    # db.session.commit()


@app.route('/')
@app.route('/homepage')
def homepage():
    # users = User.query.all()
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        utente = User(username=form.username.data, email=form.email.data, password=form.password.data,
                      first_name=form.first_name.data, last_name=form.last_name.data, birthday=form.birthday.data,
                      phone=form.phone.data, role='utente')
        db.session.add(utente)
        db.session.commit()
        flash("Your account has been created!", 'success')
        return redirect(url_for('login'))
    else:
        print(form.errors)
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password = form.password.data
        if user is not None:
            if user.password == password:
                session['username'] = user.username
                session['role'] = user.role
                session['id'] = user.id
                flash("Logged in", 'success')
                return redirect(url_for('homepage'))
            else:
                flash("password non corretta", 'error')
        else:
            flash("utente non registrato", 'error')
    return render_template("login.html", form=form)


@app.route('/carrello')
def carrello():
    return render_template("carrello.html")


@app.route('/collabora')
def collabora():
    return render_template("collabora.html")


@app.route('/cambia')
def cambia():
    listaBox = Boxes.query.filter_by(foodOfferer=session.get('username')).all()
    return render_template("cambia.html", listaBox=listaBox)


@app.route('/handleCambia', methods=['POST'])
def handleCambia():
    for key in request.form.iterkeys():
        if not key.isdigit() or not request.form[key].isdigit():
                continue
        value = int(request.form[key])
        box = Boxes.query.filter_by(id=int(key)).first()
        box.setQuantity(value)
        return redirect(url_for('cambia'))



@app.route('/offerer1')
def offerer1():
    return render_template("offerer1.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()
    # appFlask.run(debug=True)
