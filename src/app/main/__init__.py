from flask import Blueprint
from . import routes # noqa: E402, F401

bp = Blueprint("main", __name__)
