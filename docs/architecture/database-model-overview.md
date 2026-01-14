-8<-- "../_includes/header.md"


# Database Model Overview  
*Understanding how your relational data is structured*

---

## Why does this project use a relational database?

Most real-world applications need to store information that is connected in meaningful ways.  
A relational database lets you:

- store structured data  
- define relationships between tables  
- enforce data integrity  
- run powerful queries  
- evolve your schema over time  

This template uses **SQLAlchemy** (Python ORM) and **Alembic** (migrations) to give you a professional, flexible database layer.

---

## The Core Models

The template includes several models that work together to support a wide range of projects.

### **User**
Represents someone who can log in to the system.

Fields include:
- username  
- email  
- password hash  
- role (member, staff, admin)

### **Role**
Defines what a user is allowed to do.

Examples:
- member  
- staff  
- admin  

This supports **Role-Based Access Control (RBAC)**.

---

## Generic Item System

The template uses a flexible model called **Item**.  
This can represent:

- a book  
- a video  
- a product  
- a task  
- an asset  
- a document  
- anything your project needs  

### **Item**
Common fields include:
- title  
- description  
- year  
- identifier (ISBN, DOI, product code, etc.)  
- item type  
- creators  
- categories  

### **ItemType**
A lookup table for types of items.

Examples:
- Book  
- Video  
- Magazine  
- Audio  
- Document  

Students can add as many types as they need.

---

## Many-to-Many Relationships

Two important relationships use association tables:

### **Item ↔ Creator**
An item can have many creators (authors, directors, artists).  
A creator can be linked to many items.

### **Item ↔ Category**
An item can belong to many categories (genres, subjects, tags).  
A category can contain many items.

These patterns are common in real systems and help students understand relational modelling.

---

## Why this model is flexible

Because the model uses generic names like **Item**, **Creator**, and **Category**, students can adapt it to any project without rewriting the database layer.

Examples:
- Inventory system → Item = Product  
- Task manager → Item = Task  
- Media database → Item = MediaItem  
- Research archive → Item = Document  

The relational structure stays the same.

---

## Migrations with Alembic

Alembic allows you to:

- create new tables  
- modify existing tables  
- track schema changes over time  

This is essential for professional development and helps students learn how real systems evolve.

---

## Where to go next

Explore:

- `src/app/db/models.py` — the actual model definitions  
- `src/app/main/forms.py` — forms that interact with the database  
- `src/app/main/queries.py` — example search queries  
