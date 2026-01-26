"""
CSV Importer Service for the Online Library Catalogue.

Handles:
- Validating CSV structure
- Creating Item, Creator, Category, ItemType records
- Avoiding duplicates
- Returning a structured summary report
"""

import csv
from datetime import datetime
from ...db.models import db, Item, Creator, Category, ItemType


REQUIRED_HEADERS = {"title", "description", "year", "item_type", "creators", "categories", "identifier"}


def import_csv(file_stream):
    """
    Import catalogue items from a CSV file.

    Expected columns:
    - title
    - description
    - year
    - item_type
    - creators (comma-separated)
    - categories (comma-separated)
    - identifier (unique)

    Returns a dict summary.
    """

    reader = csv.DictReader(file_stream)

    # Validate headers
    missing = REQUIRED_HEADERS - set(reader.fieldnames or [])
    if missing:
        return {"error": f"Missing required columns: {', '.join(missing)}"}

    added = 0
    skipped = 0
    errors = []

    for row in reader:
        try:
            identifier = row["identifier"].strip()

            # Skip duplicates
            if Item.query.filter_by(identifier=identifier).first():
                skipped += 1
                continue

            # ItemType
            item_type_name = row["item_type"].strip()
            item_type = ItemType.query.filter_by(name=item_type_name).first()
            if not item_type:
                item_type = ItemType(name=item_type_name)
                db.session.add(item_type)

            # Creators
            creator_names = [c.strip() for c in row["creators"].split(",") if c.strip()]
            creators = []
            for name in creator_names:
                creator = Creator.query.filter_by(name=name).first()
                if not creator:
                    creator = Creator(name=name)
                    db.session.add(creator)
                creators.append(creator)

            # Categories
            category_names = [c.strip() for c in row["categories"].split(",") if c.strip()]
            categories = []
            for name in category_names:
                category = Category.query.filter_by(name=name).first()
                if not category:
                    category = Category(name=name)
                    db.session.add(category)
                categories.append(category)

            # Create Item
            item = Item(
                title=row["title"].strip(),
                description=row["description"].strip(),
                year=int(row["year"]) if row["year"].isdigit() else None,
                identifier=identifier,
                created_at=datetime.utcnow(),
                item_type=item_type,
            )

            item.creators = creators
            item.categories = categories

            db.session.add(item)
            added += 1

        except Exception as e:
            errors.append(str(e))

    db.session.commit()

    return {
        "added": added,
        "skipped": skipped,
        "errors": errors,
    }

