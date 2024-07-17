#!/usr/bin/python3
"""Application configuration settings"""
from datetime import timedelta
import os


class Config:
    """Base configuration class with default settings"""
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
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
