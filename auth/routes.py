from flask_bcrypt import Bcrypt
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, login_required
from classes.login import LoginForm
from classes.user import User
from myutils import get_user_data_by_email


bcrypt = Bcrypt()
Auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@Auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_data = get_user_data_by_email(email)
        if user_data and password == user_data['password']:
            user = User(user_data)
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', form=form)


@Auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('auth.login'))
