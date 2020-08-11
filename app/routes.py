from flask import render_template
from app import flask_app
from app.forms import LoginForm

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

@flask_app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)

