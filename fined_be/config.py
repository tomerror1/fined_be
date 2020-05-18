import os
import json
with open("ect/config.json") as config_file:
        config = json.load(config_file)
class Config:
    # Security 
    SECRET_KEY = config.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
