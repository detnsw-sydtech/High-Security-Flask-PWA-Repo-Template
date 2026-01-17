"""
API blueprint package.

Provides JSON endpoints for the Online Library Catalogue:
- items
- creators
- categories
- search

All routes are read-only for this reference implementation.
"""

from flask import Blueprint

bp = Blueprint("api", __name__, url_prefix="/api")

# Import routes AFTER bp is defined to avoid circular imports
from . import routes  # noqa: E402,F401
