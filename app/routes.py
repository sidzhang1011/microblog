from flask import render_template
from app import flask_app

count = 0

@flask_app.route('/')
@flask_app.route('/index')
def index():
    global count
    count += 1
    user = {'username': 'Sid'}
    user['count'] = str(count)
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
