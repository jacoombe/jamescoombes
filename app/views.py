#!/usr/bin/env python
from app import app
from flask import render_template, request, session, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': { 'nickname': 'Sophie' },
            'body': 'I have a medium/little tumtum!!!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)    

@app.route('/config')
def config():
    print(repr(app.config))
    return repr(app.config)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """This is the login function. This logs on a user. There is only
    one and it is derived from the config file"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))    