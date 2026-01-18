"""
Database models for the STHS High‑Security Flask PWA Template.

All models inherit from `db.Model`, which comes from the shared
SQLAlchemy instance defined in `src/app/extensions.py`.

Students can add new models here as their project grows.
"""

from datetime import datetime
from ..extensions import db


# ------------------------------------------------------------
# Example: ItemType (e.g., Book, Movie, Article)
# ------------------------------------------------------------
class ItemType(db.Model):
    __tablename__ = "item_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    items = db.relationship("Item", back_populates="item_type")

    def __repr__(self):
        return f"<ItemType {self.name}>"


# ------------------------------------------------------------
# Example: Creator (e.g., Author, Director)
# ------------------------------------------------------------
class Creator(db.Model):
    __tablename__ = "creators"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    items = db.relationship("Item", secondary="item_creators", back_populates="creators")

    def __repr__(self):
        return f"<Creator {self.name}>"


# ------------------------------------------------------------
# Example: Category (e.g., Fiction, Science, History)
# ------------------------------------------------------------
class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    items = db.relationship("Item", secondary="item_categories", back_populates="categories")

    def __repr__(self):
        return f"<Category {self.name}>"


# ------------------------------------------------------------
# Example: Item (core catalogue object)
# ------------------------------------------------------------
class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key to ItemType
    item_type_id = db.Column(db.Integer, db.ForeignKey("item_types.id"))
    item_type = db.relationship("ItemType", back_populates="items")

    # Many-to-many relationships
    creators = db.relationship("Creator", secondary="item_creators", back_populates="items")
    categories = db.relationship("Category", secondary="item_categories", back_populates="items")

    def __repr__(self):
        return f"<Item {self.title}>"


# ------------------------------------------------------------
# Association Tables (many-to-many)
# ------------------------------------------------------------

item_creators = db.Table(
    "item_creators",
    db.Column("item_id", db.Integer, db.ForeignKey("items.id"), primary_key=True),
    db.Column("creator_id", db.Integer, db.ForeignKey("creators.id"), primary_key=True),
)

item_categories = db.Table(
    "item_categories",
    db.Column("item_id", db.Integer, db.ForeignKey("items.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True),
)
