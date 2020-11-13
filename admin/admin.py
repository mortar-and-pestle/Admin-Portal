from flask import Flask, render_template, url_for, flash, redirect, session
from forms import adminSelector
app = Flask(__name__)

app.config['SECRET_KEY'] = '33332323232'
admins = [
    {"admin": "support admin"},
    {"admin": "finance admin"},
    {"admin": "sales admin"},
    {"admin": "hr admin"},
    {"admin": "tech admin"}]

current_admin = ''

@app.route('/', methods = ['GET', 'POST'])
##@app.route('/home')
##def hello():
##    return render_template('home.html', admins = admins)

@app.route("/selectAdmin", methods = ['GET', 'POST'])
def selectAdmin():
    form = adminSelector()
    if form.validate_on_submit():
        value = dict(form.adminType.choices).get(form.adminType.data)
        session['current_admin'] = value
        if value == 'ADMIN':
            flash('Okaaay chief', 'success')
            return redirect(url_for('admin'))
        elif value == 'FINANCE_ADMIN':
            return redirect(url_for('finance'))
        elif value == 'HR_ADMIN':
            return redirect(url_for('hr'))
        elif value == 'SALES_ADMIN':
            return redirect(url_for('sales'))
        elif value == 'TECHNOLOGY_ADMIN':
            return redirect(url_for('technology'))
        else:
            flash("Sorry chief, you aren't admin enough to enter", 'danger')
            return redirect(url_for('selectAdmin'))
    return render_template('admins.html', form = form)
@app.route('/admin')
def admin():
    current_admin = session.get('current_admin', None)
    if current_admin != 'ADMIN':
        return redirect(url_for('selectAdmin'))
    return render_template('supportPortal.html')

@app.route('/finance')
def finance():
    current_admin = session.get('current_admin', None)
    if current_admin != 'FINANCE_ADMIN':
        return redirect(url_for('selectAdmin'))
    return render_template('financePortal.html')

@app.route('/hr')
def hr():
    current_admin = session.get('current_admin', None)
    if current_admin != 'HR_ADMIN':
        return redirect(url_for('selectAdmin'))
    return render_template('hrPortal.html')

@app.route('/sales')
def sales():
    current_admin = session.get('current_admin', None)
    if current_admin != 'SALES_ADMIN':
        return redirect(url_for('selectAdmin'))
    return render_template('salesPortal.html')

@app.route('/technology')
def technology():
    current_admin = session.get('current_admin', None)
    if current_admin != 'TECHNOLOGY_ADMIN':
        return redirect(url_for('selectAdmin'))
    return render_template('technologyPortal.html')


if __name__ == '__main__':
    app.run(debug = True)

