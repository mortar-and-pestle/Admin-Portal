from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
class adminSelector(FlaskForm):
    adminType = SelectField('types: ', choices = [('Support', 'ADMIN'), ('Finance', 'FINANCE_ADMIN'),
                            ('Sales', 'SALES_ADMIN'), ('HR', 'HR_ADMIN'), ('Technology', 'TECH_ADMIN'),('User', 'REGULAR_USER')])
    submit =  SubmitField("submit selection")
