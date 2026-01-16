"""
Main application routes.

This blueprint contains the core public-facing pages of the application.
At this stage of the project, the focus is on helping students understand:

1. How Flask renders HTML templates.
2. How JSON responses work.
3. How blueprints organise related functionality.
4. How health endpoints support CI, monitoring, and security scanning.

These routes form the "front door" of the application and demonstrate
the basic request/response flow in a clean, minimal way.
"""

from flask import render_template, jsonify
from . import bp


@bp.get("/")
def index() -> str:
    """
    Render the main landing page.

    This route demonstrates how Flask uses templates to generate HTML.
    The template file `index.html` lives in the application's templates
    directory and can contain any HTML, CSS, or JavaScript needed for
    the user interface.

    Later, students can expand this page to include:
    - navigation
    - dynamic content
    - PWA installation prompts
    - Tailwind‑styled components
    """
    return render_template("index.html")


@bp.get("/health")
def health():
    """
    Health check endpoint.

    This route is used by:
    - CI workflows (01-ci.yml)
    - Wapiti dynamic security scanning
    - Monitoring tools or uptime checks

    It returns a simple JSON object confirming that the main blueprint
    is functioning correctly. Keeping this endpoint lightweight ensures
    it remains reliable even under load.
    """
    return jsonify({"status": "ok", "component": "main"})


@bp.get("/info")
def info():
    """
    Basic diagnostic endpoint.

    This route returns a small JSON payload that helps students
    understand:
    - how JSON responses are structured
    - how blueprints can expose useful metadata
    - how to design simple API-style endpoints

    It is intentionally minimal and safe for early development.
    """
    return jsonify(
        {
            "app": "STHS Flask PWA",
            "blueprint": "main",
            "version": "1.0",
        }
    )
