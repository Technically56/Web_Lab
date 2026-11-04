from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ForgetPasswordForm, LoginForm

@app.route('/')
@app.route('/index')
@app.route('/index/<username>')
@app.route('/<username>')
def index(username=None):
    user = {'username': username or 'John Doe'}
    return render_template('index.html', title='Home', user=user)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/forget_password', methods=['GET', 'POST'])
def forget_password():
    form = ForgetPasswordForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('forget_password.html',
    title='Forget Password',
    form=form)