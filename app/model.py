from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import uuid


db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())

    def __repr__(self) -> str:
        return f"Note('{self.content}')"