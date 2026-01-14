# ERD vs SQLAlchemy Models  
*A side‑by‑side comparison to help you understand how diagrams become code*

---

## Why this guide exists

An Entity Relationship Diagram (ERD) shows the structure of your database visually.  
Your SQLAlchemy models implement that structure in Python.

This guide helps you see how each part of the ERD maps directly to the code in:
```
src/app/db/models.py
```

Understanding this mapping is essential for designing clean, relational applications.

---

# 1. Role ↔ User (One‑to‑Many)

## ERD
```
ROLE ||--o{ USER
```

## SQLAlchemy
**Foreign key:**
```python
role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
```

**Relationships:**
```python
Role.users  = db.relationship("User", back_populates="role")
User.role  = db.relationship("Role", back_populates="users")
```

**Meaning:**  
One role can be assigned to many users.  
Each user belongs to exactly one role.

---

# 2. ItemType ↔ Item (One‑to‑Many)

## ERD
```text
ITEMTYPE ||--o{ ITEM
```

## SQLAlchemy
**Foreign key:**
```python
item_type_id = db.Column(db.Integer, db.ForeignKey("item_type.id"))
```

**Relationships:**
```python
ItemType.items  = db.relationship("Item", back_populates="item_type")
Item.item_type = db.relationship("ItemType", back_populates="items")
```

**Meaning:**  
One item type (Book, Video, etc.) can be linked to many items.

---

# 3. Item ↔ Creator (Many‑to‑Many)

## ERD
```text
ITEM ||--o{ ITEM_CREATOR }o--|| CREATOR
```

## SQLAlchemy
**Association table:**
```python
item_creator = db.Table(
"item_creator",
db.Column("item_id", db.Integer, db.ForeignKey("item.id"), primary_key=True),
db.Column("creator_id", db.Integer, db.ForeignKey("creator.id"), primary_key=True),
)
```

**Relationships:**
```python
Item.creators  = db.relationship("Creator", secondary=item_creator, back_populates="items")
Creator.items  = db.relationship("Item", secondary=item_creator, back_populates="creators")
```

**Meaning:**  
An item can have many creators.  
A creator can be linked to many items.  
The association table stores the relationship.

---

# 4. Item ↔ Category (Many‑to‑Many)

## ERD
```text
ITEM ||--o{ ITEM_CATEGORY }o--|| CATEGORY
```

## SQLAlchemy
**Association table:**
```python
item_category = db.Table(
"item_category",
db.Column("item_id", db.Integer, db.ForeignKey("item.id"), primary_key=True),
db.Column("category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True),
)
```

**Relationships:**
```python
Item.categories  = db.relationship("Category", secondary=item_category, back_populates="items")
Category.items  = db.relationship("Item", secondary=item_category, back_populates="categories")
```

**Meaning:**  
An item can belong to many categories.  
A category can contain many items.

---

# 5. Table Fields: ERD vs Model Code

## Example: Item

### ERD
```text
ITEM {
int id PK
string title
text description
int year
string identifier
int item_type_id FK
text internal_notes
datetime created_at
datetime updated_at
}
```

### SQLAlchemy
```python
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(255), nullable=False)
description = db.Column(db.Text)
year = db.Column(db.Integer)
identifier = db.Column(db.String(100))
item_type_id = db.Column(db.Integer, db.ForeignKey("item_type.id"))
internal_notes = db.Column(db.Text)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

**Meaning:**  
Every field in the ERD maps directly to a column in the SQLAlchemy model.

---

# 6. Summary

- The ERD shows the **structure** of your database.  
- The SQLAlchemy models **implement** that structure in Python.  
- One‑to‑many relationships use **foreign keys**.  
- Many‑to‑many relationships use **association tables**.  
- This project’s ERD and models match **exactly**, making the system clean, normalised, and easy to extend.

---


