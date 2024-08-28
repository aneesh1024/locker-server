
class Config:
    """Base Configuration"""
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'