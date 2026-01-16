from flask import render_template
from . import bp

@bp.route("/offline")
def offline():
    return "<h1>You are offline</h1>"
