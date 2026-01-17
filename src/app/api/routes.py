"""
Extensive API routes for the Online Library Catalogue.

Supports:
- full‑text search
- filtering by category, creator, item type, year range
- pagination (page, per_page)
- sorting (title, year, created_at)
- JSON serialisation of Items and related models

Designed to scale to 20,000+ records.
"""

from flask import request, jsonify
from sqlalchemy import or_, and_
from . import bp
from ..db.models import Item, Creator, Category, ItemType
from ..db import db


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def _pagination_params():
    """Extract and clamp pagination parameters."""
    page = max(int(request.args.get("page", 1)), 1)
    per_page = int(request.args.get("per_page", 20))
    per_page = max(1, min(per_page, 100))  # clamp to [1, 100]
    return page, per_page


def _sort_params():
    """Extract sorting parameters."""
    sort = request.args.get("sort", "created_at")
    direction = request.args.get("direction", "desc")

    valid_fields = {
        "title": Item.title,
        "year": Item.year,
        "created_at": Item.created_at,
    }

    field = valid_fields.get(sort, Item.created_at)
    if direction == "asc":
        return field.asc()
    return field.desc()


def _item_to_dict(item: Item) -> dict:
    """Serialise an Item model to JSON."""
    return {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "year": item.year,
        "identifier": item.identifier,
        "item_type": item.item_type.name if item.item_type else None,
        "creators": [c.name for c in item.creators],
        "categories": [c.name for c in item.categories],
        "created_at": item.created_at.isoformat() if item.created_at else None,
        "updated_at": item.updated_at.isoformat() if item.updated_at else None,
    }


# ------------------------------------------------------------
# Core catalogue endpoint
# ------------------------------------------------------------

@bp.get("/items")
def list_items():
    """
    List items with:
    - search
    - filtering
    - sorting
    - pagination
    """

    page, per_page = _pagination_params()
    sort_clause = _sort_params()

    q = request.args.get("q", "").strip()
    category = request.args.get("category")
    creator = request.args.get("creator")
    item_type = request.args.get("type")
    year_min = request.args.get("year_min")
    year_max = request.args.get("year_max")

    query = Item.query

    # -----------------------------
    # Search
    # -----------------------------
    if q:
        like = f"%{q}%"
        query = query.filter(
            or_(
                Item.title.ilike(like),
                Item.description.ilike(like),
                Item.identifier.ilike(like),
            )
        )

    # -----------------------------
    # Filtering
    # -----------------------------
    if category:
        query = query.join(Item.categories).filter(Category.name == category)

    if creator:
        query = query.join(Item.creators).filter(Creator.name == creator)

    if item_type:
        query = query.join(Item.item_type).filter(ItemType.name == item_type)

    if year_min:
        query = query.filter(Item.year >= int(year_min))

    if year_max:
        query = query.filter(Item.year <= int(year_max))

    # Avoid duplicates when joining many-to-many
    query = query.distinct()

    # -----------------------------
    # Sorting
    # -----------------------------
    query = query.order_by(sort_clause)

    # -----------------------------
    # Pagination
    # -----------------------------
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify(
        {
            "items": [_item_to_dict(i) for i in pagination.items],
            "pagination": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total_items": pagination.total,
                "total_pages": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev,
            },
            "filters": {
                "q": q or None,
                "category": category,
                "creator": creator,
                "type": item_type,
                "year_min": year_min,
                "year_max": year_max,
            },
            "sort": request.args.get("sort", "created_at"),
            "direction": request.args.get("direction", "desc"),
        }
    )


# ------------------------------------------------------------
# Single item
# ------------------------------------------------------------

@bp.get("/items/<int:item_id>")
def get_item(item_id: int):
    item = Item.query.get_or_404(item_id)
    return jsonify(_item_to_dict(item))


# ------------------------------------------------------------
# Supporting lists
# ------------------------------------------------------------

@bp.get("/categories")
def list_categories():
    categories = Category.query.order_by(Category.name.asc()).all()
    return jsonify({"categories": [{"id": c.id, "name": c.name} for c in categories]})


@bp.get("/creators")
def list_creators():
    creators = Creator.query.order_by(Creator.name.asc()).all()
    return jsonify({"creators": [{"id": c.id, "name": c.name} for c in creators]})


@bp.get("/item-types")
def list_item_types():
    types = ItemType.query.order_by(ItemType.name.asc()).all()
    return jsonify({"item_types": [{"id": t.id, "name": t.name} for t in types]})
