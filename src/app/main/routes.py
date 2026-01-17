"""
Main blueprint routes for the Online Library Catalogue.

Includes:
- Landing page (/)
- Health and info endpoints
- HTMX-powered catalogue partial (/catalogue)
- Full catalogue page (/catalogue/full)
- Debug JSON endpoint (/catalogue/debug)
"""

from flask import render_template, jsonify, request
from sqlalchemy import or_
from . import bp
from ..db.models import Item, Category, Creator, ItemType


# ------------------------------------------------------------
# Landing page
# ------------------------------------------------------------

@bp.get("/")
def index():
    """Render the main landing page."""
    return render_template("index.html")


# ------------------------------------------------------------
# Full catalogue page (non-HTMX)
# ------------------------------------------------------------

@bp.get("/catalogue/full")
def catalogue_full():
    """
    Render the full catalogue page.

    This page loads the same HTMX-powered interface as index.html,
    but provides a dedicated standalone URL for browsing.
    """
    return render_template("catalogue.html")


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
# Debug JSON endpoint
# ------------------------------------------------------------

@bp.get("/catalogue/debug")
def catalogue_debug():
    """
    Return raw JSON data for debugging, testing, and DAST tools.
    Replace BOOKS with your actual dataset source.
    """
    try:
        from .data import BOOKS
    except ImportError:
        return jsonify({"error": "BOOKS dataset not found"}), 500

    return jsonify(BOOKS)


# ------------------------------------------------------------
# HTMX Catalogue Partial
# ------------------------------------------------------------

@bp.get("/catalogue")
def catalogue_partial():
    """
    Return an HTML partial containing:
    - item cards
    - pagination controls

    This endpoint is called by HTMX from index.html and catalogue.html.
    """

    # Pagination
    try:
        page = int(request.args.get("page", 1))
    except ValueError:
        page = 1

    page = max(page, 1)

    # Filters
    q = request.args.get("q", "").strip()
    category = request.args.get("category")
    creator = request.args.get("creator")
    item_type = request.args.get("type")
    sort = request.args.get("sort", "created_at")
    direction = request.args.get("direction", "desc")

    query = Item.query

    # Search
    if q:
        like = f"%{q}%"
        query = query.filter(
            or_(
                Item.title.ilike(like),
                Item.description.ilike(like),
                Item.identifier.ilike(like),
            )
        )

    # Category filter
    if category:
        query = query.join(Item.categories).filter(Category.name == category)

    # Creator filter
    if creator:
        query = query.join(Item.creators).filter(Creator.name == creator)

    # Item type filter
    if item_type:
        query = query.join(Item.item_type).filter(ItemType.name == item_type)

    # Sorting
    sort_fields = {
        "title": Item.title,
        "year": Item.year,
        "created_at": Item.created_at,
    }

    sort_column = sort_fields.get(sort, Item.created_at)
    sort_clause = sort_column.asc() if direction == "asc" else sort_column.desc()

    query = query.order_by(sort_clause).distinct()

    # Pagination
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
