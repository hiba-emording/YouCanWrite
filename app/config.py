#!/usr/bin/python3
"""config file"""
from datetime import timedelta
import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:itsme@localhost/youcanwritedb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True
    SCHEDULER_API_PREFIX = '/scheduler'
    SESSION_PERMANENT = True
    SESSION_TYPE = "filesystem"
    SESSION_FILE_THRESHOLD = 250
    PERMANENT_SESSION_LIFETIME = timedelta(hours=10)  
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'youcanwriteofficial@gmail.com'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
