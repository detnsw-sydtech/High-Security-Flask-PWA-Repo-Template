"""
Database models for the STHS Flask PWA.

This module defines the SQLAlchemy ORM (Object Relational Mapping) models
used throughout the application. Each class represents a database table,
and each attribute represents a column.

Students should understand the following concepts:

1. SQLAlchemy ORM
   - Allows Python classes to map directly to database tables.
   - Avoids writing raw SQL for common operations.

2. db.Model
   - Base class for all models.
   - Provided by SQLAlchemy and initialised in the application factory.

3. Relationships
   - one-to-many (e.g., Role → Users)
   - many-to-many (e.g., Item ↔ Creator, Item ↔ Category)
   - SQLAlchemy automatically loads related objects.

4. Association Tables
   - Used for many-to-many relationships.
   - Do not have their own model class.
   - Only contain foreign keys.

These models are intentionally generic so students can adapt them to
different project contexts (library catalogue, asset manager, product
inventory, etc.).
"""

from datetime import datetime
from . import db


# ---------------------------------------------------------------------------
# Association tables (many-to-many)
# ---------------------------------------------------------------------------

item_creator = db.Table(
    "item_creator",
    db.Column(
        "item_id",
        db.Integer,
        db.ForeignKey("item.id"),
        primary_key=True,
    ),
    db.Column(
        "creator_id",
        db.Integer,
        db.ForeignKey("creator.id"),
        primary_key=True,
    ),
)

item_category = db.Table(
    "item_category",
    db.Column(
        "item_id",
        db.Integer,
        db.ForeignKey("item.id"),
        primary_key=True,
    ),
    db.Column(
        "category_id",
        db.Integer,
        db.ForeignKey("category.id"),
        primary_key=True,
    ),
)


# ---------------------------------------------------------------------------
# Role model
# ---------------------------------------------------------------------------

class Role(db.Model):
    """
    Represents a user role (e.g., member, staff, admin).

    Demonstrates:
    - one-to-many relationship (Role → Users)
    - use of back_populates for bidirectional relationships
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    users = db.relationship("User", back_populates="role")

    def __repr__(self) -> str:
        return f"<Role {self.name}>"


# ---------------------------------------------------------------------------
# User model
# ---------------------------------------------------------------------------

class User(db.Model):
    """
    Represents an application user.

    Demonstrates:
    - foreign keys (role_id)
    - one-to-many relationship (User → Role)
    - timestamp fields (created_at)
    - storing hashed passwords (never store raw passwords)
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    role = db.relationship("Role", back_populates="users")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User {self.username}>"


# ---------------------------------------------------------------------------
# ItemType model
# ---------------------------------------------------------------------------

class ItemType(db.Model):
    """
    Represents a type or category of item (e.g., Book, Video, Audio).

    Demonstrates:
    - one-to-many relationship (ItemType → Items)
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    items = db.relationship("Item", back_populates="item_type")

    def __repr__(self) -> str:
        return f"<ItemType {self.name}>"


# ---------------------------------------------------------------------------
# Item model
# ---------------------------------------------------------------------------

class Item(db.Model):
    """
    Represents a generic item in the system.

    This model is intentionally flexible so students can reuse it for:
    - library items (books, DVDs)
    - products
    - digital assets
    - tasks or activities

    Demonstrates:
    - foreign keys (item_type_id)
    - many-to-many relationships (creators, categories)
    - timestamp fields (created_at, updated_at)
    """

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    year = db.Column(db.Integer)
    identifier = db.Column(db.String(100))

    item_type_id = db.Column(db.Integer, db.ForeignKey("item_type.id"), nullable=False)
    item_type = db.relationship("ItemType", back_populates="items")

    creators = db.relationship(
        "Creator",
        secondary=item_creator,
        back_populates="items",
    )

    categories = db.relationship(
        "Category",
        secondary=item_category,
        back_populates="items",
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    internal_notes = db.Column(db.Text)

    def __repr__(self) -> str:
        return f"<Item {self.title} ({self.id})>"


# ---------------------------------------------------------------------------
# Creator model
# ---------------------------------------------------------------------------

class Creator(db.Model):
    """
    Represents a creator (author, director, artist, etc.).

    Demonstrates:
    - many-to-many relationship (Creator ↔ Items)
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)

    items = db.relationship(
        "Item",
        secondary=item_creator,
        back_populates="creators",
    )

    def __repr__(self) -> str:
        return f"<Creator {self.name}>"


# ---------------------------------------------------------------------------
# Category model
# ---------------------------------------------------------------------------

class Category(db.Model):
    """
    Represents a category, subject, genre, or tag.

    Demonstrates:
    - many-to-many relationship (Category ↔ Items)
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    items = db.relationship(
        "Item",
        secondary=item_category,
        back_populates="categories",
    )

    def __repr__(self) -> str:
        return f"<Category {self.name}>"
