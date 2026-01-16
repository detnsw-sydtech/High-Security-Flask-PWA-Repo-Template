from flask import Blueprint
from . import routes # noqa: E402, F401

bp = Blueprint("auth", __name__, url_prefix="/auth")


