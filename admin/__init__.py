from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#Create instance of Flask Class passing in __name__
#__name__ is the name of the current Python module. The app needs to know where
#it’s located to set up some paths, and __name__ is a convenient way to tell it that.
app = Flask (__name__)
#Config is a subclass of a Dictionary. It acts just like a dictionary
#This dict sets certain config values for this Flask app
#Specifically, setting the secret key to a certain value.
#A secret key that will be used for securely signing the session cookie and
#can be used for any other security related needs by extensions or your application.
app.config['SECRET_KEY'] = '9e844a33d2830730d50f1ba5f80ee4c844364'
#Point app to DB location
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'
login_manager.login_message_category = 'info'

from admin import routes
