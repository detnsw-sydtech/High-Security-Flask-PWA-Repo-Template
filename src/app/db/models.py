# src/app/db/models.py

from datetime import datetime
from . import db


# Association tables for many-to-many relationships
item_creator = db.Table(
    "item_creator",
    db.Column("item_id", db.Integer, db.ForeignKey("item.id"), primary_key=True),
    db.Column("creator_id", db.Integer, db.ForeignKey("creator.id"), primary_key=True),
)

item_category = db.Table(
    "item_category",
    db.Column("item_id", db.Integer, db.ForeignKey("item.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True),
)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  # member, staff, admin
    users = db.relationship("User", back_populates="role")

    def __repr__(self) -> str:
        return f"<Role {self.name}>"

    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    role = db.relationship("Role", back_populates="users")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    
class ItemType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)  # Book, Video, etc.
    description = db.Column(db.String(255))

    items = db.relationship("Item", back_populates="item_type")

    def __repr__(self) -> str:
        return f"<ItemType {self.name}>"

    
class Item(db.Model):
    """
    Generic item that can represent books, videos, audio, etc.
    Students can reuse this as Product, Asset, Task, etc.
    """

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    year = db.Column(db.Integer)
    identifier = db.Column(db.String(100))  # ISBN, DOI, catalogue number, etc.

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
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Example of a field that might be staff-only
    internal_notes = db.Column(db.Text)

    def __repr__(self) -> str:
        return f"<Item {self.title} ({self.id})>"


class Creator(db.Model):
    """
    Author, director, artist, etc.
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


class Category(db.Model):
    """
    Subject, genre, topic, tag, etc.
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
