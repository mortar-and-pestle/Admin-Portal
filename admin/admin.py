from flask import Flask, render_template, url_for, flash, redirect, session
from forms import LoginForm

#Create instance of Flask Class passing in __name__
#__name__ is the name of the current Python module. The app needs to know where
#it’s located to set up some paths, and __name__ is a convenient way to tell it that.
app = Flask(__name__)

#Config is a subclass of a Dictionary. It acts just like a dictionary
#This dict sets certain config values for this Flask app
#Specifically, setting the secret key to a certain value.
#A secret key that will be used for securely signing the session cookie and
#can be used for any other security related needs by extensions or your application.
app.config['SECRET_KEY'] = '33332323232'
current_admin = ''

#Setup route with @app.route decorator
#Note:methods indicate the type of HTTP requestions expected.
#If methods is not included, GET is the default method.
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('links'))
    #render_template will render the template located in the templates folder
    #Conifiguration with the Jinja2 template engine is taken care of by Flask
    return render_template('login.html', form = form)
@app.route('/links')
def links():
    return render_template('links.html')

#If this file is being ran directly(not imported), then start execution by
#called app.run. The debug is so errors will show on the webpage
if __name__ == '__main__':
    app.run(debug = True)
