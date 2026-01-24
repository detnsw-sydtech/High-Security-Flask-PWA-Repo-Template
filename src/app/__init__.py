"""
Application factory for the STHS High‑Security Flask PWA Template.

This file is the *entry point* for the Flask application.
It creates the Flask app, loads configuration, initialises extensions,
and registers all blueprints.

Students should understand this file before modifying any part of the project.
"""

from flask import Flask
from .extensions import db, apply_security_headers   # centralised SQLAlchemy + security middleware

from dotenv import load_dotenv
import os


def create_app():
    """
    Create and configure the Flask application.

    This function is called the *application factory*.
    """

    # ---------------------------------------------------------
    # 1. Load .env BEFORE creating the app
    #
    # This ensures environment variables are available before
    # Flask reads them into its configuration.
    #
    # Priority order becomes:
    #   1. GitHub/Codespaces secrets (real production key)
    #   2. System environment variables
    #   3. .env fallback (local development)
    # ---------------------------------------------------------
    load_dotenv()

    # ---------------------------------------------------------
    # 2. Create the Flask application object
    # ---------------------------------------------------------
    app = Flask(__name__)

    # ---------------------------------------------------------
    # 3. Apply configuration explicitly
    #
    # Avoid app.config.from_mapping(os.environ) because it dumps
    # *every* OS environment variable into Flask config, which can
    # cause naming collisions and unexpected behaviour.
    #
    # Instead, load only the keys your app actually needs.
    # ---------------------------------------------------------
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "cde259759ba72e5840e22c132b6a155e55f0f0d9ae776671194c3ad9c91a7975"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "sqlite:///dev.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ---------------------------------------------------------
    # 4. Initialise extensions
    # ---------------------------------------------------------
    db.init_app(app)

    # ---------------------------------------------------------
    # 5. Register blueprints
    # ---------------------------------------------------------
    from .main import bp as main_bp
    from .auth import bp as auth_bp
    from .pwa import bp as pwa_bp
    from .security import bp as security_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(pwa_bp)
    app.register_blueprint(security_bp)

    # ---------------------------------------------------------
    # 6. Apply global security headers
    #
    # This middleware hardens every response by adding:
    #   - X-Frame-Options (prevents clickjacking)
    #   - X-Content-Type-Options (prevents MIME sniffing)
    #   - Referrer-Policy (limits information leakage)
    #   - Permissions-Policy (restricts powerful browser APIs)
    #
    # This directly addresses Nikto findings and models secure
    # defaults for students building production-ready Flask apps.
    # ---------------------------------------------------------
    @app.after_request
    def add_security_headers(response):
        return apply_security_headers(response)

    # ---------------------------------------------------------
    # 7. Return the configured app
    # ---------------------------------------------------------
    return app
