from flask import render_template, request, Blueprint
from fined_be.models import Module, LearningUnit

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
    modules = Module.query.all()
    return render_template('dashboard.html', modules=modules)


@main.route('/investition')
def investition():
    learning_units = LearningUnit.query.all()
    return render_template('investition.html', learning_units=learning_units)


@main.route('/about')
def about():
    return render_template('about.html')