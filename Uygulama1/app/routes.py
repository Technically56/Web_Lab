from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index(username=None):
    user = {'username': username or 'John Doe'}
    return render_template('index.html', title='Home', user=user)


@app.route('/mylibrary')
def mylibrary():
    books = [
        {"title": "Book 1", "author": "Author 1", "is_read": True},
        {"title": "Book 2", "author": "Author 2", "is_read": False},
        {"title": "Book 3", "author": "Author 3", "is_read": True},
        {"title": "Book 4", "author": "Author 4", "is_read": False}
        ]




    return render_template('library.html', title='My Library', books=books, username='Can',current_url='mylibrary')
