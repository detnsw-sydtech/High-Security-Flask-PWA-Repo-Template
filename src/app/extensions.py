"""
Application-wide extension instances.

This file creates *one* instance of each Flask extension used by the app.
Extensions are created here (without an app) and then initialised inside
the application factory using `extension.init_app(app)`.

Why this pattern?
-----------------
- Prevents circular imports
- Keeps the app factory clean and readable
- Ensures all blueprints and models share the same extension instances
- Mirrors real-world Flask application structure
"""

from flask_sqlalchemy import SQLAlchemy

# ------------------------------------------------------------
# Database (SQLAlchemy)
# ------------------------------------------------------------
# This instance is shared across the entire application.
# Models import `db` from this file, and the app factory
# calls `db.init_app(app)` to attach it to the Flask app.
db = SQLAlchemy()
