"""
CSV Exporter Service for the Online Library Catalogue.
"""

import csv
from io import StringIO
from ...db.models import Item


def export_csv():
    """
    Export all catalogue items to CSV.
    Returns a StringIO object containing CSV data.
    """

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "title",
        "description",
        "year",
        "item_type",
        "creators",
        "categories",
        "identifier",
    ])

    for item in Item.query.all():
        writer.writerow([
            item.title,
            item.description or "",
            item.year or "",
            item.item_type.name if item.item_type else "",
            ", ".join(c.name for c in item.creators),
            ", ".join(c.name for c in item.categories),
            item.identifier,
        ])

    output.seek(0)
    return output

