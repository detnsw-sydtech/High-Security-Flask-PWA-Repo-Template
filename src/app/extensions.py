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


# ------------------------------------------------------------
# Security Headers Middleware
# ------------------------------------------------------------
# These headers harden the application against common web attacks.
# They are applied to *every* response via app.after_request(apply_security_headers)
#
# Why these headers matter:
# - X-Frame-Options: Prevents clickjacking by blocking <iframe> embedding.
# - X-Content-Type-Options: Stops MIME-type sniffing attacks.
# - Referrer-Policy: Limits how much information the browser sends in the Referer header.
# - Permissions-Policy: Restricts access to powerful browser features (camera, mic, etc.).
#
# This middleware directly addresses Nikto findings and models secure defaults
# for students building production-ready Flask applications.
# ------------------------------------------------------------

def apply_security_headers(response):
    # Prevent clickjacking
    response.headers["X-Frame-Options"] = "DENY"

    # Prevent MIME-type sniffing
    response.headers["X-Content-Type-Options"] = "nosniff"

    # Restrict how much referrer information is leaked
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    # Disable access to sensitive browser APIs unless explicitly allowed
    response.headers["Permissions-Policy"] = (
        "geolocation=(), microphone=(), camera=(), fullscreen=(), payment=()"
    )

    return response
