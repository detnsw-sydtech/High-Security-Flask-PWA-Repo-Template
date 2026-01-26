# 📚 Database Modelling & Migrations
---
A reference architecture for SE12 students using the High‑Security Flask PWA Template


This guide explains how to design, register, migrate, and manage relational database models inside the template. 
It also covers **CSV** import/export and **RBAC**‑protected **CRUD** operations.

The goal is to give you a **repeatable, industry‑aligned workflow** that you can use for your own projects.

**NOTES:**

**CSV** is an abbreviation for the "Comma Separated Value" file type.

**RBAC** is an abbreviation for "Role Based Access Control", a protective mechanism for database access.

**CRUD** is an abbreviation for Create, Read, Update, and Delete, representing the four fundamental, persistent operations for managing data in relational databases and applications. These operations allow users to add new records, view existing data, modify information, and remove data


## 1. 🧱 Where Models Live
All database models live in:
```code
src/app/db/models.py
```
This file already contains example models:
- ```ItemType```
- ```Creator```
- ```Category```
- ```Item```
- ```item_creators``` (association table, allows for 1 to many relationship to be established)
- ```item_categories``` (association table, allows for 1 to many relationship to be established)

You can add your own additional models here as their project grows.

## 2. 🧱 Understanding the Existing Model Structure
The template already demonstrates:
### ✔ One‑to‑many
```ItemType → Item```

### ✔ One‑to‑many
```Item ↔ Creator```

```Item ↔ Category```

### ✔ Association tables
```item_creators```

```item_categories```

### ✔ Common fields
```id```, ```title```, ```description```, ```year```, ```created_at```

This gives you a strong foundation for building your own relational schemas.

## 3. 🏗 Registering Models With the Application

**SQLAlchemy**  is a widely-used Python **SQL** toolkit and **ORM** that provides a full suite of enterprise-level persistence patterns, designed for efficient and high-performing database access.

The SQLAlchemy instance is created in:
```bash
src/app/extensions.py
```

The app factory imports models so Flask‑Migrate can detect them.

You must ensure:

- new models are defined in ```src/app/db/models.py```

- the file is imported in the app factory (already handled in the template)

This ensures migrations pick up all models automatically.

**NOTES:**

**SQL** is an abbreviation for Structured Query Language and it is the common language used to interact with databases.

The link to SQLAlchemy on PyPi is below:

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/)

**ORM** is an abbreviation for Object-Relational Mapper and it is the tool that enables the database designer to create the design of the tables, fields and relationships in the database.


## 4. 🔧 Creating and Running Database Migrations

We use **Flask‑Migrate (Alembic)** to track schema changes. 

The link to Flask-Migrate on PyPi is below:

[Flask-Migrate](https://pypi.org/project/Flask-Migrate/)

### Initial setup (done once per project)
```
flask db init
```

### Generate a migration after editing models
```
flask db migrate -m "Describe your change"
```

### Apply the migration
```
flask db upgrade
```

This is the **canonical workflow** students will use every time they change a model.


## 5. 🔐 RBAC‑Protected CRUD Operations

Routes for adding, editing, and deleting items should be protected using the existing RBAC decorators.

Example pattern:

- Admin + Librarian → add/edit items

- Admin → delete items

- All authenticated users → view items

This will teach you how to:

- protect routes

- check roles

- return JSON for debugging

- build forms or API endpoints

## 6. 📥 CSV Import (Admin‑Only)

CSV import is a powerful teaching tool.

Typical workflow:

1. Admin uploads a CSV file
2. Backend validates the file
3. Parse rows using Python’s csv module
4. Convert rows into model instances
5. Commit to the database
6. Return a summary (added, skipped, errors)

This teaches you how to do:

- file upload handling
- data validation
- bulk inserts
- idempotency (avoid duplicates)

Sample CSV templates are widely available for viewing on the web. 
You can also think back to importing of CSV files into databases and spreadsheets during the Stage 5 Computing Technology course.

## 7. 📤 CSV Export (Admin + Librarian)


## 8. 🖥 Building the Catalogue UI




## 9. 🔌 JSON API Endpoints (Optional but Powerful)




## 10. 🧪 Automated Testing




## 11. 🗂 Recommended Folder Structure
Suggested Directory Tree
```tree
src/
  app/
    db/
      models.py
    routes/
      catalog.py
      admin.py
    templates/
      catalog/
        list.html
        detail.html
        upload.html
    static/
    services/
      csv_importer.py
      csv_exporter.py
      search.py
```

## 🎯 Summary Workflow (Student‑Friendly)

1. Define models in src/app/db/models.py
2. Register models in the app factory
3. Generate migrations
4. Apply migrations
5. Build RBAC‑protected CRUD routes
6. Implement CSV import/export
7. Build catalogue UI
8. Add JSON API endpoints
9. Write automated tests
10. Document your work


This is the reference architecture you’ll use for all future database‑driven projects.
