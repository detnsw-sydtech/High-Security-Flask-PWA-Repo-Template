from flask_sqlalchemy import SQLAlchemy

# Global SQLAlchemy instance used across the application.
# It is initialised in create_app() inside src/app/__init__.py.
db = SQLAlchemy()
