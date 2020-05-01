from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from fined_be.config import Config

app = Flask(__name__)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# declace where to login to the login manager
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # has to be down here, to avoid circular errors
    # we are import blueprint instances
    from fined_be.users.routes import users
    from fined_be.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(main)

    return app