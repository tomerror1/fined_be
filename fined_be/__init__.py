from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Security 
app.config['SECRET_KEY'] = '02e063133a16ed2428bdc742cefffa74'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# has to be down here, to avoid circular errors
from fined_be import routes 