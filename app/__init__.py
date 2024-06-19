#!/usr/bin/python3
"""init package"""
from flask import Flask
from .extensions import db, bcrypt, migrate
from .scheduler import init_scheduler
from flask_apscheduler import APScheduler
from .config import Config
from .auth import auth
from .routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(api, url_prefix='/api')

    init_scheduler(app)

    return app
