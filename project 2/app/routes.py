# app/routes.py
from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, SignupForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    signup_form = SignupForm()

    if login_form.validate_on_submit() and login_form.submit.data:
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and user.check_password(login_form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')

    if signup_form.validate_on_submit() and signup_form.submit.data:
        user = User(email=signup_form.email.data)
        user.set_password(signup_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully.', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', login_form=login_form, signup_form=signup_form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))
