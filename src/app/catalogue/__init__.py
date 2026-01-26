from flask import Blueprint

bp = Blueprint("catalogue", __name__, url_prefix="/catalogue")

from . import routes  # noqa: E402
