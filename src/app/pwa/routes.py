"""
Routes for the PWA (Progressive Web App) components.

This blueprint serves three key pieces of the PWA architecture:

1. manifest.json
   - Tells the browser how the app should behave when "installed".
   - Includes icons, theme colours, and app metadata.

2. service-worker.js
   - Controls caching, offline behaviour, and background updates.
   - Must be served from the same origin and path scope as the app.

3. offline fallback page
   - Displayed when the user has no network connection and the
     service worker cannot retrieve a cached page.

Each route below is intentionally simple so students can clearly see
how Flask exposes static files and how PWAs integrate with a backend.
"""

from flask import send_from_directory, jsonify
from . import bp


@bp.get("/manifest.json")
def manifest():
    """
    Serve the PWA manifest file.

    Flask normally serves static files from /static automatically,
    but PWAs require the manifest to be available at a predictable
    top-level path (e.g., /manifest.json). This route exposes it
    explicitly so browsers can find it during installation.
    """
    return send_from_directory(
        "static",
        "manifest.json",
        mimetype="application/manifest+json",
    )


@bp.get("/service-worker.js")
def service_worker():
    """
    Serve the service worker script.

    Service workers must be served from the same origin and path
    scope as the pages they control. By exposing it at
    /service-worker.js, the worker can manage the entire site.

    The file itself lives in static/js/service-worker.js.
    """
    return send_from_directory(
        "static/js",
        "service-worker.js",
        mimetype="application/javascript",
    )


@bp.get("/offline")
def offline() -> str:
    """
    Offline fallback page.

    When the user loses network access and the service worker cannot
    retrieve a cached page, this simple HTML response is shown.

    Later, students can replace this with a full template.
    """
    return "<h1>You are offline</h1>"


@bp.get("/health")
def health():
    """
    Health check endpoint.

    Used by:
    - CI workflows
    - Wapiti dynamic security scanning
    - Monitoring tools

    Returns a simple JSON object indicating that the PWA blueprint
    is functioning correctly.
    """
    return jsonify({"status": "ok", "component": "pwa"})
