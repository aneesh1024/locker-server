from flask import Blueprint, request, jsonify
from app.model import Note, db
import os
from sqlalchemy import desc

main_bp = Blueprint('main',__name__)


CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")

# Decorator for password validation
def require_password(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if auth_header and auth_header.startswith("Bearer "):
            password = auth_header.split(" ")[1]
            
            # Validate the password
            if password == CORRECT_PASSWORD:
                return f(*args, **kwargs)
                
        # If password is missing or incorrect
        return jsonify({"message": "Unauthorized"}), 401
    wrapper.__name__ = f.__name__
    return wrapper

@main_bp.route('/')
def index():
    return{"msg": "Hello, API"}, 200

@main_bp.route('/add', methods=['POST'])
@require_password
def add_content():
    note = request.get_json()
    print(note)
    if 'note' not in note:
        return jsonify({"message":"Note not added"}),500
    print(note['note'])
    if len(note['note']) > 500:
        return jsonify({"error":"Note is too long"}), 500
    new_note = Note(content=note['note'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message":"Note added"}),200

@main_bp.route('/getall', methods=['GET'])
@require_password
def getallnotes():
    notes = Note.query.order_by(desc(Note.created_at)).all()
    return jsonify({'notes':[{'id':note.id, 'content':note.content,'createdAt':note.created_at} for note in notes]}), 200

@main_bp.route('/note/<id>',methods=['GET'])
@require_password
def getnote(id):
    note = Note.query.get(id)
    return jsonify({'note':{'id':note.id, 'content':note.content,'createdAt':note.created_at}}), 200

@main_bp.route('/delete/<id>', methods=['DELETE'])
@require_password
def deleteNote(id):
    note = Note.query.get(id)
    if note is None:
        return jsonify({"error":"Note not found"}), 500
    db.session.delete(note)
    db.session.commit();
    return jsonify({"message": "Note deleted successfully"}), 200
