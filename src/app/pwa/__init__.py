"""
PWA blueprint package.

Defines the blueprint object (`bp`) and then imports the route handlers.
Importing routes at the bottom avoids circular import issues because the
blueprint exists before routes reference it.
"""

from flask import Blueprint

bp = Blueprint("pwa", __name__, url_prefix="/pwa")

# Import routes AFTER bp is defined to avoid circular imports
from . import routes  # noqa: E402,F401
