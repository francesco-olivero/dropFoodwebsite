from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=1, max=25)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=25)])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=20)])
    birthday = StringField('Birthday', validators=[DataRequired()])
    phone = StringField('Phone number', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Registrati')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=1, max=20), DataRequired()])
    submit = SubmitField('Login')


