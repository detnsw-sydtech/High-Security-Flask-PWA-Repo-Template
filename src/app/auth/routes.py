from . import bp

@bp.route("/login")
def login():
    return "<h1>Login page placeholder</h1>"

@bp.route("/logout")
def logout():
    return "<h1>Logout placeholder</h1>"
