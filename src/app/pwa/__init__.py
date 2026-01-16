from flask import Blueprint
from . import routes  # noqa: E402, F401

bp = Blueprint("pwa", __name__, url_prefix="/pwa")
