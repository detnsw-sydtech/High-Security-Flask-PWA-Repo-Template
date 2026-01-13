from flask import Flask
from flask_migrate import Migrate

from .db import db
from .security import init_security_headers

# Blueprints
from .auth import auth_bp
from .main import main_bp
from .pwa import pwa_bp


def create_app():
    app = Flask(__name__)

    # ---------------------------------------------------------
    # Core configuration
    # ---------------------------------------------------------
    app.config["SECRET_KEY"] = "change-me-in-production"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ---------------------------------------------------------
    # Initialise database + migrations
    # ---------------------------------------------------------
    db.init_app(app)
    Migrate(app, db)

    # ---------------------------------------------------------
    # Register blueprints
    # ---------------------------------------------------------
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)
    app.register_blueprint(pwa_bp)

    # ---------------------------------------------------------
    # Security headers (CSP, HSTS, etc.)
    # ---------------------------------------------------------
    init_security_headers(app)

    return app
