from flask import jsonify
from . import bp

@bp.route("/health")
def health():
    return jsonify({"status": "ok"})
