from flask import render_template, request, Blueprint
from fined_be.models import Module, LearningUnit

from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    modules = Module.query.all()
    user = current_user
    return render_template('dashboard.html', modules=modules, user=user, title='Dashboard')


@main.route('/investition')
@login_required
def investition():
    learning_units = LearningUnit.query.all()
    return render_template('investition.html', learning_units=learning_units, title='Investition')


@main.route('/about')
@login_required
def about():
    return render_template('about.html')