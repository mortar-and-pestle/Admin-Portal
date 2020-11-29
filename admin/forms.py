from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, PasswordField, BooleanField
from wtforms.widgets import PasswordInput
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators =[DataRequired(), Length(min = 2, max = 25)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 6, max = 30)], widget=PasswordInput(hide_value=False))
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
