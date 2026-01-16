"""
Security and diagnostics routes.

This blueprint provides operational endpoints that help monitor and
validate the security posture of the application. These routes do not
perform authentication or authorisation — those belong in the `auth`
blueprint. Instead, they support:

1. Health checks for CI and uptime monitoring.
2. Wapiti dynamic security scanning.
3. Basic diagnostics that help students understand how Flask handles
   JSON responses and blueprint organisation.

All routes are intentionally simple and safe for early development.
"""

from flask import jsonify
from . import bp


@bp.get("/health")
def health():
    """
    Health check endpoint.

    Used by:
    - CI workflows (01-ci.yml)
    - Wapiti DAST scanning
    - Monitoring tools

    Returns a simple JSON object indicating that the security
    blueprint is functioning correctly.
    """
    return jsonify({"status": "ok", "component": "security"})


@bp.get("/headers")
def headers():
    """
    Return a minimal set of recommended security headers.

    This endpoint does NOT enforce these headers — it simply returns
    them as JSON so students can see what a secure configuration
    might look like. Later, these can be applied globally using
    `after_request` handlers in the application factory.
    """
    return jsonify(
        {
            "Content-Security-Policy": "default-src 'self'",
            "X-Frame-Options": "DENY",
            "X-Content-Type-Options": "nosniff",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        }
    )


@bp.get("/info")
def info():
    """
    Basic diagnostic endpoint.

    Helps students understand:
    - how JSON responses work
    - how blueprints organise functionality
    - how to structure operational endpoints

    This endpoint is safe and contains no sensitive information.
    """
    return jsonify(
        {
            "blueprint": "security",
            "purpose": "operational diagnostics",
            "version": "1.0",
        }
    )
