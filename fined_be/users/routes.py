from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from fined_be import db, bcrypt
from fined_be.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from fined_be.models import User
from fined_be.users.utils import save_picture

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Dein Account wurde erstellt. Du kannst dich ab sofort einloggen.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user exists and password is valid in comparison to db
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # function takes a user, and boolean for remember
            login_user(user, remember=form.remember.data)
            # if next parameter exists it will be that route (want to access specific side after login)
            next_page = request.args.get('next')
            # route to next page if exists else to home
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Anmeldung fehlgeschlagen. Bitte Email und Passwort prüfen.', 'danger')
    return render_template('login.html', title='Register', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))



@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file 
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Update erfolgreich.', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename="profile_pics/" + current_user.image_file)
    return render_template('account.html', title='Account',
        image_file=image_file, form=form)