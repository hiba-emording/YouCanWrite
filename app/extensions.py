#!/usr/bin/python3
"""Initialize Flask extensions"""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_session import Session
from flask_login import LoginManager



db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
Session = Session()
login_manager = LoginManager()

