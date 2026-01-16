"""
Authentication routes.

This blueprint contains the routes responsible for handling user login
and logout actions. At this stage of the project, the logic is kept
intentionally simple so students can clearly understand:

1. How HTML forms send data to Flask using GET and POST.
2. How Flask retrieves form data using `request.form`.
3. How redirects work using `redirect()` and `url_for()`.
4. How blueprints organise related functionality.
5. How placeholder logic can later be replaced with real authentication.

These routes DO NOT perform real authentication yet. They simply
demonstrate the structure and flow of an auth system.
"""

from flask import request, redirect, url_for, jsonify
from . import bp


@bp.get("/login")
def login_form() -> str:
    """
    Display a placeholder login form.

    In a real application, this would render a template such as:
        return render_template("auth/login.html")

    For now, we return simple HTML so students can focus on the
    request/response flow without needing templates.
    """
    return "<h1>Login page placeholder</h1>"


@bp.post("/login")
def login_submit():
    """
    Handle login form submission.

    This route demonstrates:
    - how POST requests send form data
    - how Flask retrieves fields using `request.form.get()`
    - how to perform a redirect after successful login

    The logic here is intentionally minimal:
    - If both username and password are provided, we redirect to the
      main index page.
    - Otherwise, we return a simple error message.

    Later, this function can be expanded to:
    - validate credentials
    - check a database
    - set session cookies
    - handle login errors more gracefully
    """
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # Placeholder logic only — no real authentication yet.
    if username and password:
        return redirect(url_for("main.index"))

    return "<h1>Invalid login (placeholder)</h1>", 400


@bp.get("/logout")
def logout() -> str:
    """
    Placeholder logout route.

    In a real application, this would:
    - clear the user's session
    - redirect them to a login or home page

    For now, it simply returns a placeholder message.
    """
    return "<h1>Logout placeholder</h1>"


@bp.get("/health")
def health():
    """
    Health check endpoint.

    Used by:
    - CI workflows
    - Wapiti DAST scanning
    - Monitoring tools

    Returns a simple JSON object indicating that the auth blueprint
    is functioning correctly.
    """
    return jsonify({"status": "ok", "component": "auth"})
