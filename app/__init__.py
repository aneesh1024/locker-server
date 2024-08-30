from flask import Flask
from config import Config
from app.model import db
from flask_cors import CORS
from app.routes import main_bp
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

load_dotenv()
app.register_blueprint(main_bp, url_prefix='/')

with app.app_context():
    db.create_all()