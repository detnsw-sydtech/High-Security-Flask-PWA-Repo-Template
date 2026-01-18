"""
Basic test to verify that the database initialises correctly.

This test ensures:
- the Flask app factory returns a valid app
- the SQLAlchemy extension is initialised
- tables can be created without errors
"""

from src.app import create_app
from src.app.extensions import db


def test_database_initialises():
    app = create_app()

    # Use the app context so SQLAlchemy can access the app
    with app.app_context():
        try:
            db.create_all()
            db.drop_all()
        except Exception as e:
            raise AssertionError(f"Database failed to initialise: {e}")
