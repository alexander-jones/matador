from flask import request, render_template, flash, redirect, url_for, current_app
from flask_table import Table, Col
from app import app, db
from app.models import User
from .forms import LoginForm, RegistrationForm
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

import bcrypt

def have_user():
    return hasattr(current_app, 'user') and current_app.user is not None

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Unknown User'} 
    if have_user():
        user = db.session.merge(current_app.user)
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not have_user():
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                user_input = form.username_or_email.data
                current_app.user = User.query.filter(or_(User.email == user_input, User.name == user_input)).first()
                return redirect(url_for('index'))
            except IntegrityError:
                flash('No user found with the name or email {0}'.format(user_input))
        return render_template('login.html', form=form)
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if not have_user():
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                salt = bcrypt.gensalt()
                user = User(name = form.username.data, email = form.email.data, password = bcrypt.hashpw(form.password.data.encode('utf-8') + salt, salt), salt = salt)
                db.session.add(user)
                db.session.commit()
                current_app.user = user
                return redirect(url_for('index'))
            except IntegrityError:
                flash('A user is already registered with the email {0}'.format(form.email.data))
        return render_template('register.html', form=form)
    return redirect(url_for('index'))