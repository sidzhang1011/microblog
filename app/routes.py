#coding=utf-8

from flask import render_template, flash, redirect, url_for
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

@flask_app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		msg = 'Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data)
		print(msg)
		flash(msg)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

