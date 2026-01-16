from flask import Blueprint
from . import routes  # noqa: E402, F401

bp = Blueprint("security", __name__, url_prefix="/security")
