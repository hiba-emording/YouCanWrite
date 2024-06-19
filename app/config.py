#!/usr/bin/python3
"""config file"""

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:itsme@localhost/youcanwritedb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True
    SCHEDULER_API_PREFIX = '/scheduler'
