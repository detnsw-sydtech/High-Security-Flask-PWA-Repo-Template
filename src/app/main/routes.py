"""
Main blueprint routes for the Online Library Catalogue.

Includes:
- Landing page (/)
- Health and info endpoints
"""

from flask import render_template, jsonify
from . import bp


# ------------------------------------------------------------
# Landing page
# ------------------------------------------------------------

@bp.get("/")
def index():
    """Render the main landing page."""
    return render_template("index.html")


# ------------------------------------------------------------
# Health + Info (used by diagnostics and DAST)
# ------------------------------------------------------------

@bp.get("/health")
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok"})


@bp.get("/info")
def info():
    """Basic application info."""
    return jsonify(
        {
            "app": "STHS Flask PWA",
            "version": "1.0",
            "description": "Online Library Catalogue",
        }
    )
