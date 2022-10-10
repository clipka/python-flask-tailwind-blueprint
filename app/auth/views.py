from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db
from werkzeug.urls import url_parse


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(id=db.get_id(),
                    username=form.username.data.lower(),
                    email=form.email.data.lower(),
                    hashed_password="")
        user.set_password(form.password.data)
        db.add(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html.jinja',
                           title='Register',
                           form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    nologin = False
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.get_user_by_email(form.email.data.lower())
        if user is None or not user.check_password(form.password.data):
            nologin = True
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('profile')
            return redirect(next_page)
    return render_template('auth/login.html.jinja', title='Sign In',
                           form=form, message=nologin)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
