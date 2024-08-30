import os

class Config:
    """Base Configuration"""
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'
    