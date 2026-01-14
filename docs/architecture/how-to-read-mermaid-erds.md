--8<-- "../_includes/header.md"


# How to Read Mermaid ERDs  
*A student‑friendly guide to understanding Entity Relationship Diagrams*

---

## What is an ERD?

An **Entity Relationship Diagram (ERD)** shows how tables in a relational database connect to each other.  
It helps you understand:

- what tables exist  
- what fields they contain  
- how they relate  
- which fields are primary keys (PK)  
- which fields are foreign keys (FK)  

Mermaid is a simple text‑based way to draw ERDs that GitHub can render automatically.

---

## Basic Mermaid ERD Syntax

A Mermaid ERD looks like this:
```text
erDiagram
TABLE1 ||--o{ TABLE2 : "relationship"
```

The symbols show the type of relationship:

- `||` means “one”
- `o{` means “many”

So:
```
||--o{
```

means **one‑to‑many**.

---

## Reading One‑to‑Many

Example:
```text
ITEMTYPE ||--o{ ITEM : "has many"
```

This means:

- One ItemType  
- can be linked to many Items  

In SQLAlchemy, this is represented with:

- a foreign key in `Item`  
- a relationship in both models  

---

## Reading Many‑to‑Many

Mermaid shows many‑to‑many using a **link table**:
```
ITEM ||--o{ ITEM_CREATOR : "links"
CREATOR ||--o{ ITEM_CREATOR : "links"
```

This means:

- an Item can have many Creators  
- a Creator can be linked to many Items  
- the relationship is stored in the `ITEM_CREATOR` table  

This matches how relational databases actually work.

---

## Reading Table Definitions

Mermaid lets you list fields inside each table:
```text
ITEM {
int id PK
string title
int item_type_id FK
}
```

- `PK` = primary key  
- `FK` = foreign key  

This helps you see the structure at a glance.

---

## Why ERDs Matter

ERDs help you:

- understand the database before writing code  
- design clean, normalised tables  
- avoid duplication  
- plan your search queries  
- communicate your design to others  

They are essential for any relational project.

---

## Where to go next

Check out:

- `relational-erd.md` — the full ERD for this project  
- `relational-relationships-overview.md` — how relationships work  


--8<-- "../_includes/footer.md"
