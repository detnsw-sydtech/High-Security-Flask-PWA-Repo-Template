"""
Application factory for the STHS High‑Security Flask PWA Template.

This file is the *entry point* for the Flask application.
It creates the Flask app, loads configuration, and registers all blueprints.

Students should understand this file before modifying any part of the project.
"""

from flask import Flask


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
    # 2. Register blueprints
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
    # 3. Return the configured app
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
