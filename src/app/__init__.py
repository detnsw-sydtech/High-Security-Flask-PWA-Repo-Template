# src/app/__init__.py

from flask import Flask
from .db import db
from .auth import auth_bp
from .main import main_bp
from .pwa import pwa_bp
from .security import init_security_headers


def create_app():
    app = Flask(__name__)

    # Basic config – students can adjust per project
    app.config["SECRET_KEY"] = "change-me-in-production"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialise extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)
    app.register_blueprint(pwa_bp)

    # Security headers
    init_security_headers(app)

    return app

