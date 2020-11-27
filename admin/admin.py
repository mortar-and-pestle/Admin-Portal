from flask import Flask, render_template, url_for, flash, redirect, session
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '33332323232'
current_admin = ''

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('links'))

    return render_template('login.html', form = form)
@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(debug = True)

