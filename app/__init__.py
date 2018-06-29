#importing flask
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#defining app and giving it a variable name
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
#takes in app that is being used and the database
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' 

from app import routes

bootstrap = Bootstrap(app)
