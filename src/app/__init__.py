"""
Application factory for the STHS High‑Security Flask PWA Template.

This file is the *entry point* for the Flask application.
It creates the Flask app, loads configuration, initialises extensions,
and registers all blueprints.

Students should understand this file before modifying any part of the project.
"""

from flask import Flask
from .extensions import db   # centralised SQLAlchemy instance

# Load environment variables from .env
from dotenv import load_dotenv
import os


def create_app():
    """
    Create and configure the Flask application.

    This function is called the *application factory*.
    Instead of creating the Flask app at the top level of the file,
    we wrap it in a function so that:

    - the app can be created multiple times (useful for testing)
    - configuration can be applied cleanly
    - blueprints can be registered in a predictable order
    - the project stays modular and easy to extend

    Flask will automatically look for:
    - HTML templates inside:  src/app/templates/
    - static files inside:    src/app/static/

    Returns:
        A fully configured Flask application instance.
    """

    # ---------------------------------------------------------
    # 1. Create the Flask application object
    # ---------------------------------------------------------
    app = Flask(__name__)

    # ---------------------------------------------------------
    # 2. Load configuration from environment variables
    #
    # This ensures settings such as:
    # - SQLALCHEMY_DATABASE_URI
    # - SECRET_KEY
    # - any future config values
    #
    # are correctly loaded before extensions are initialised.
    # ---------------------------------------------------------
    load_dotenv()                         # Load .env into the environment
    app.config.from_mapping(os.environ)   # Load ALL environment variables into Flask config

    # ---------------------------------------------------------
    # 3. Initialise extensions
    #
    # Extensions provide reusable functionality such as:
    # - database access (SQLAlchemy)
    # - authentication
    # - caching
    #
    # Each extension is created once (in extensions.py) and then
    # "attached" to the app here using init_app().
    # ---------------------------------------------------------
    db.init_app(app)

    # ---------------------------------------------------------
    # 4. Register blueprints
    #
    # Each blueprint represents a logical "section" of the app.
    # This keeps the project modular and easy to navigate.
    #
    # Blueprints currently included:
    # - main:     The PWA landing page (index.html)
    # - auth:     Login/logout routes (future expansion)
    # - pwa:      PWA-specific routes (offline page, install helpers)
    # - security: Health checks and future security utilities
    #
    # Students can add new blueprints (e.g., "api") without touching
    # the rest of the application.
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
    # 5. Return the configured app
    #
    # Flask will now use:
    # - templates from src/app/templates/
    # - static files from src/app/static/
    # - routes from each blueprint
    #
    # This structure mirrors real-world Flask applications and
    # supports a secure, scalable PWA architecture.
    # ---------------------------------------------------------
    return app
