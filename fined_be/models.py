from datetime import datetime
from fined_be import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    # backref - leads back to user 

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')" 


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.String(400), unique=False, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default_module.jpg")
    learning_units = db.relationship('LearningUnit', backref='module', lazy=True)

    def __repr__(self):
        return f"Module('{self.name}')"

class LearningUnit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(400), unique=False, nullable=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)

    def __repr__(self):
        return f"LearningUnit('{self.name}', '{self.module_id}')"