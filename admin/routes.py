from flask import Flask, render_template, url_for, flash, redirect, session
from admin import app, db
from admin.forms import LoginForm
from admin.models import User
from flask_login import login_user, current_user, logout_user, login_required

current_admin = ''

#Setup route with @app.route decorator
#Note:methods indicate the type of HTTP requestions expected.
#If methods is not included, GET is the default method.
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('links'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            login_user(user, remember = form.remember.data)
            if user.type != "":
                return redirect(url_for('links'))
            else:
                flash('You do not have admin status! Please contact IT to be assigned an admin status.', 'danger')
                return redirect(url_for('logout'))
        else:
            flash('Login failed. Check username and password.', 'danger')

    #render_template will render the template located in the templates folder
    #Conifiguration with the Jinja2 template engine is taken care of by Flask
    return render_template('login.html',title = 'Login', form = form)

@app.route('/links')
@login_required
def links():
    user = User.query.filter_by(username = current_user.username).first()
    return render_template('links.html', title = "Links", user = user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
