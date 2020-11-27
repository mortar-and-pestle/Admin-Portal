from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, PasswordField, BooleanField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
