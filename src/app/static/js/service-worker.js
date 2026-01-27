@bp.get("/service-worker.js")
def service_worker():
    return send_from_directory(
        "static/js",
        "service-worker.js",
        mimetype="application/javascript",
        cache_timeout=0
    )
