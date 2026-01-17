"""
Main blueprint routes for the Online Library Catalogue.

Includes:
- Landing page (/)
- Health and info endpoints
- HTMX-powered catalogue partial (/catalogue)
"""

from flask import render_template, jsonify, request
from sqlalchemy import or_
from . import bp
from ..db.models import Item


# ------------------------------------------------------------
# Landing page
# ------------------------------------------------------------

@bp.get("/")
def index():
    """Render the main landing page."""
    return render_template("index.html")


# ------------------------------------------------------------
# Health + Info (used by diagnostics and DAST)
# ------------------------------------------------------------

@bp.get("/health")
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok"})


@bp.get("/info")
def info():
    """Basic application info."""
    return jsonify(
        {
            "app": "STHS Flask PWA",
            "version": "1.0",
            "description": "Online Library Catalogue",
        }
    )


# ------------------------------------------------------------
# HTMX Catalogue Partial
# ------------------------------------------------------------

@bp.get("/catalogue")
def catalogue_partial():
    """
    Return an HTML partial containing:
    - item cards
    - pagination controls

    This endpoint is called by HTMX from index.html.
    """

    # Pagination
    try:
        page = int(request.args.get("page", 1))
    except ValueError:
        page = 1

    page = max(page, 1)

    # Search
    q = request.args.get("q", "").strip()

    query = Item.query

    if q:
        like = f"%{q}%"
        query = query.filter(
            or_(
                Item.title.ilike(like),
                Item.description.ilike(like),
                Item.identifier.ilike(like),
            )
        )

    # Order newest first
    query = query.order_by(Item.created_at.desc())

    # Paginate (12 items per page)
    pagination = query.paginate(page=page, per_page=12, error_out=False)

    # Serialise items for template
    items = [
        {
            "title": item.title,
            "description": item.description,
            "year": item.year,
            "creators": [c.name for c in item.creators],
            "categories": [c.name for c in item.categories],
        }
        for item in pagination.items
    ]

    return render_template(
        "partials/item_list.html",
        items=items,
        pagination=pagination,
        query=q,
    )
