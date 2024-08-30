import os

class Config:
    """Base Configuration"""
    SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRES_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'
    