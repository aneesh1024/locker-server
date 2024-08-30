from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import secrets

db = SQLAlchemy()

def createUUID() -> str:
    return secrets.token_hex(2) + ""+secrets.token_hex(2)+""+secrets.token_hex(2)+""+secrets.token_hex(2)
    

class Note(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, default=createUUID())
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())

    def __repr__(self) -> str:
        return f"Note('{self.content}')"