"""
Catalogue blueprint routes for the Online Library Catalogue.

Includes:
- Full catalogue page (/catalogue/full)
- HTMX-powered catalogue partial (/catalogue)
- Item detail page (/catalogue/<id>)
- Debug JSON endpoint (/catalogue/debug)
- CSV import/export endpoints (placeholders for future work)
"""

from flask import Blueprint, render_template, jsonify, request
from sqlalchemy import or_
from ..db.models import Item, Category, Creator, ItemType

bp = Blueprint("catalogue", __name__, url_prefix="/catalogue")


# ------------------------------------------------------------
# Full catalogue page (non-HTMX)
# ------------------------------------------------------------

@bp.get("/full", endpoint="catalogue_full")
def catalogue_full():
    """
    Render the full catalogue page.

    This page loads the HTMX-powered interface and acts as the
    main entry point for browsing the catalogue.
    """
    return render_template("catalogue/index.html")


# ------------------------------------------------------------
# HTMX Catalogue Partial
# ------------------------------------------------------------

@bp.get("/", endpoint="catalogue_partial")
def catalogue_partial():
    """
    Return an HTML partial containing:
    - item cards
    - pagination controls

    This endpoint is called by HTMX from index.html and catalogue/index.html.
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


# ------------------------------------------------------------
# Item Detail Page (placeholder)
# ------------------------------------------------------------

@bp.get("/<int:item_id>", endpoint="catalogue_detail")
def catalogue_detail(item_id):
    """
    Display a single item's details.
    This will be expanded once the detail template is created.
    """
    item = Item.query.get_or_404(item_id)
    return render_template("catalogue/detail.html", item=item)


# ------------------------------------------------------------
# Debug JSON endpoint
# ------------------------------------------------------------

@bp.get("/debug", endpoint="catalogue_debug")
def catalogue_debug():
    """
    Temporary debug endpoint.
    Will be replaced with real DB queries once CSV import is implemented.
    """
    items = Item.query.all()
    return jsonify(
        [
            {
                "title": item.title,
                "description": item.description,
                "year": item.year,
                "creators": [c.name for c in item.creators],
                "categories": [c.name for c in item.categories],
            }
            for item in items
        ]
    )


# ------------------------------------------------------------
# CSV Import (placeholder)
# ------------------------------------------------------------

@bp.post("/import", endpoint="catalogue_import")
def catalogue_import():
    """
    CSV import endpoint (Admin-only).
    Implementation will be added once csv_importer.py is created.
    """
    return jsonify({"status": "not implemented"}), 501


# ------------------------------------------------------------
# CSV Export (placeholder)
# ------------------------------------------------------------

@bp.get("/export", endpoint="catalogue_export")
def catalogue_export():
    """
    CSV export endpoint (Admin + Librarian).
    Implementation will be added once csv_exporter.py is created.
    """
    return jsonify({"status": "not implemented"}), 501
