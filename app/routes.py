from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm
from app.forms import RegisterForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Post

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Rob' }
    return render_template('index.html', user=user, title='Home Page')

@app.route('/posts')
def posts():
    posts = [
        'This is post #1.',
        'This is post #2.',
        'We\'re looping through these posts.',
        'This is Flask!!!!'
    ]
    return render_template('posts.html', posts=posts, title='Posts')

@app.route('/login', methods=['GET', 'Post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid login credientials.')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        flash('Thanks for logging in {}!'.format(current_user.username))
        return redirect(url_for('index'))
    return render_template('login.html', form=login_form)


@app.route('/register', methods=['GET', 'Post'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        flash('Thanks {}, you are registered now!'.format(register_form.username.data))
        return redirect(url_for('index'))

    return render_template('register.html', form=register_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
