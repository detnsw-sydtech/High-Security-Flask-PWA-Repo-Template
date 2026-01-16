# src/app/db/__init__.py
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from . import routes # noqa: E402, F401

bp = Blueprint("auth", __name__, url_prefix="/auth")

db = SQLAlchemy()
