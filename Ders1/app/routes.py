from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/index/<username>')
@app.route('/<username>')
def index(username=None):
    user = {'username': username or 'John Doe'}
    return render_template('index.html', title='Home', user=user)
