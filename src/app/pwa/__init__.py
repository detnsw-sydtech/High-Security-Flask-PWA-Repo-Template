from flask import Blueprint

bp = Blueprint("pwa", __name__, url_prefix="/pwa")

from . import routes
