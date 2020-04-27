from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Security 
app.config['SECRET_KEY'] = '02e063133a16ed2428bdc742cefffa74'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# declace where to login to the login manager
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# has to be down here, to avoid circular errors
from fined_be import routes 