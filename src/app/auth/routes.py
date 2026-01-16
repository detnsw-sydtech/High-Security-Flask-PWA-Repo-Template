from flask import request, redirect, url_for, jsonify
from . import bp


@bp.get("/login")
def login_form() -> str:
    """Display a placeholder login form."""
    return "<h1>Login page placeholder</h1>"


@bp.post("/login")
def login_submit():
    """Handle login submission (placeholder)."""
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # Placeholder logic only — no real authentication yet.
    if username and password:
        return redirect(url_for("main.index"))

    return "<h1>Invalid login (placeholder)</h1>", 400


@bp.get("/logout")
def logout() -> str:
    """Placeholder logout route."""
    return "<h1>Logout placeholder</h1>"


@bp.get("/health")
def health():
    """Health check endpoint for CI, monitoring, and Wapiti."""
    return jsonify({"status": "ok", "component": "auth"})
