#!/usr/bin/python3
"""init package"""
from flask import Flask
from .extensions import db, bcrypt, migrate, Session, login_manager
from .models import User
from .scheduler import init_scheduler
from flask_apscheduler import APScheduler
from datetime import timedelta
from .config import Config
from .routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    Session.init_app(app)
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    app.register_blueprint(api, url_prefix='/')

    init_scheduler(app)

    return app
