

# Entity Relationship Diagram and Python Buildout (example only and incomplete)


## Below is the canonical ERD for the library system you and I have been refining.
It includes:
- One‑to‑Many (Role → User, ItemType → Item)
- Many‑to‑Many (Item ↔ Category, Item ↔ Creator)
- Association tables
- Attributes that match real SQLAlchemy models



## Master ERD - suggestion

```mermaid
erDiagram

    ROLE ||--o{ USER : "has many"
    ITEMTYPE ||--o{ ITEM : "has many"

    ITEM ||--o{ ITEM_CATEGORY : "has many"
    CATEGORY ||--o{ ITEM_CATEGORY : "has many"

    ITEM ||--o{ ITEM_CREATOR : "has many"
    CREATOR ||--o{ ITEM_CREATOR : "has many"

    ROLE {
        int id PK
        string name
    }

    USER {
        int id PK
        string username
        string email
        int role_id FK
    }

    ITEMTYPE {
        int id PK
        string name
    }

    ITEM {
        int id PK
        string title
        string isbn
        int item_type_id FK
    }

    CATEGORY {
        int id PK
        string name
    }

    CREATOR {
        int id PK
        string name
    }

    ITEM_CATEGORY {
        int id PK
        int item_id FK
        int category_id FK
    }

    ITEM_CREATOR {
        int id PK
        int item_id FK
        int creator_id FK
    }
```

## 1. Role ↔ User (One‑to‑Many)
### ERD insight
One role has many users
The foreign key lives on the many side (user.role_id)

models.py mapping

```python
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    users = db.relationship("User", back_populates="role")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = db.relationship("Role", back_populates="users")

```

## 2. ItemType ↔ Item (One‑to‑Many)
### ERD insight
- One ItemType has many Items
- FK lives on item.item_type_id
```
models.py mapping
```
```python
class ItemType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="item_type")


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    isbn = db.Column(db.String)

    item_type_id = db.Column(db.Integer, db.ForeignKey("item_type.id"))
    item_type = db.relationship("ItemType", back_populates="items")
```

## 3. Item ↔ Category (Many‑to‑Many)
## ERD insight
- Many‑to‑many is implemented using a join table
- Students must see that this is *two* one‑to‑many relationships

models.py mapping
```python
class ItemCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    item = db.relationship("Item", back_populates="item_categories")
    category = db.relationship("Category", back_populates="item_categories")


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    item_categories = db.relationship("ItemCategory", back_populates="category")


class Item(db.Model):
    # existing fields...
    item_categories = db.relationship("ItemCategory", back_populates="item")
```

## 4. Item ↔ Creator (Many‑to‑Many)
### ERD insight
Same pattern as Item ↔ Category.

models.py mapping
```python
class ItemCreator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    creator_id = db.Column(db.Integer, db.ForeignKey("creator.id"))

    item = db.relationship("Item", back_populates="item_creators")
    creator = db.relationship("Creator", back_populates="item_creators")


class Creator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    item_creators = db.relationship("ItemCreator", back_populates="creator")


class Item(db.Model):
    # existing fields...
    item_creators = db.relationship("ItemCreator", back_populates="item")

```


