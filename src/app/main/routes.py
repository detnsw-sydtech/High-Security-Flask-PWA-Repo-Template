from flask import render_template, jsonify
from . import bp


@bp.get("/")
def index() -> str:
    """Render the main landing page."""
    return render_template("index.html")


@bp.get("/health")
def health():
    """Health check endpoint for CI, monitoring, and Wapiti."""
    return jsonify({"status": "ok", "component": "main"})


@bp.get("/info")
def info():
    """Simple JSON endpoint for debugging and teaching."""
    return jsonify(
        {
            "app": "STHS Flask PWA",
            "blueprint": "main",
            "version": "1.0",
        }
    )
