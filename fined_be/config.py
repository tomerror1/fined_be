import os

class Config:
    # Security 
    SECRET_KEY = os.environ.get('fined_be_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('fined_be_SQLALCHEMY_DATABASE_URI')