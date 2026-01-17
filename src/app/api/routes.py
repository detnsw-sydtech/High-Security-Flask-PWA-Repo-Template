"""
API routes for the Online Library Catalogue.

All endpoints return JSON and are designed to be:
- predictable
- paginated
- filterable
- student-friendly

Query parameters:
- page:     1-based page number (default: 1)
- per_page: items per page (default: 10, max: 50)
- q:        search query (for /items and /search)
"""

from flask import request, jsonify, current_app
from sqlalchemy import or_
from . import bp
from ..db.models import Item, Creator, Category, ItemType
from ..db import db


def _get_pagination_params() -> tuple[int, int]:
    """Extract and clamp pagination parameters from the query string."""
    try:
        page = int(request.args.get("page", 1))
    except ValueError:
        page = 1

    try:
        per_page = int(request.args.get("per_page", 10))
    except ValueError:
        per_page = 10

    page = max(page, 1)
    per_page = max(1, min(per_page, 50))  # clamp to [1, 50]

    return page, per_page


def _item_to_dict(item: Item) -> dict:
    """Serialise an Item model to a JSON-friendly dict."""
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


@bp.get("/items")
def list_items():
    """
    List items with pagination and optional search.

    Query params:
    - page:     page number (default: 1)
    - per_page: items per page (default: 10, max: 50)
    - q:        optional search term (title/description)
    """
    page, per_page = _get_pagination_params()
    q = request.args.get("q", "").strip()

    query = Item.query

    if q:
        like = f"%{q}%"
        query = query.filter(
            or_(
                Item.title.ilike(like),
                Item.description.ilike(like),
            )
        )

    pagination = query.order_by(Item.created_at.desc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False,
    )

    items = [_item_to_dict(item) for item in pagination.items]

    return jsonify(
        {
            "items": items,
            "pagination": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total_items": pagination.total,
                "total_pages": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev,
            },
            "query": {"q": q or None},
        }
    )


@bp.get("/items/<int:item_id>")
def get_item(item_id: int):
    """
    Retrieve a single item by ID.
    """
    item = Item.query.get_or_404(item_id)
    return jsonify(_item_to_dict(item))


@bp.get("/categories")
def list_categories():
    """
    List all categories.
    """
    categories = Category.query.order_by(Category.name.asc()).all()
    return jsonify(
        {
            "categories": [
                {
                    "id": c.id,
                    "name": c.name,
                }
                for c in categories
            ]
        }
    )


@bp.get("/creators")
def list_creators():
    """
    List all creators.
    """
    creators = Creator.query.order_by(Creator.name.asc()).all()
    return jsonify(
        {
            "creators": [
                {
                    "id": c.id,
                    "name": c.name,
                    "birth_year": c.birth_year,
                    "death_year": c.death_year,
                }
                for c in creators
            ]
        }
    )


@bp.get("/item-types")
def list_item_types():
    """
    List all item types.
    """
    types = ItemType.query.order_by(ItemType.name.asc()).all()
    return jsonify(
        {
            "item_types": [
                {
                    "id": t.id,
                    "name": t.name,
                    "description": t.description,
                }
                for t in types
            ]
        }
    )


@bp.get("/search")
def search_items():
    """
    Search items by title/description with pagination.

    This is a convenience wrapper around /items with ?q=.
    """
    # Reuse list_items logic by delegating to it would be possible,
    # but keeping this explicit is clearer for students.
    return list_items()
