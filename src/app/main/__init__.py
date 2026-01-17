from flask import Blueprint

bp = Blueprint("main", __name__)

# Import routes AFTER bp is defined
from . import routes
