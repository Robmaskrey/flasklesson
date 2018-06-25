from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Rob' }
    #below passes the user2 variable to index and sets it to user as defined above.
    num =  2 + 2

    return render_template('index.html', user2=user,
    num=num, title='Awesome')

@app.route('/posts')
def posts():
    posts = [
        'This is post #1.',
        'This is post #2.',
        'We\'re looping through these posts.',
        'This is Flask!!!!'
    ]
    return render_template('posts.html', posts=posts, title='Posts')

@app.route('/redirect')
def goaway():
    return redirect(url_for('index'))
