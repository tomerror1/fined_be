from flask import render_template, url_for, flash, redirect
# in a package you use package.module
from fined_be import app, db, bcrypt
from fined_be.forms import RegistrationForm, LoginForm
from fined_be.models import User, Post

posts = [
    {
        'author': "Tom K.",
        'title': 'The Backend day',
        'date_posted': 'April 20, 2020',
    },
    {
        'author': "Tomas G.",
        'title': 'The Frontend Day',
        'date_posted': 'April 19, 2020',
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Dein Account wurde erstellt. Du kannst dich ab sofort einloggen.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@fined.de' and form.password.data == 'password':
            flash('Du wurdest erfolgreich angemdeldet!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Anmeldung fehlgeschlagen. Bitte Email und Passwort prüfen.', 'danger')
    return render_template('login.html', title='Register', form=form)

