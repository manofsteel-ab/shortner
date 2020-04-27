"""
Contains the Extensions to be used across application
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
# from flask_session import Session
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
bcrypt = Bcrypt()
# session = Session()
login_manager = LoginManager()
