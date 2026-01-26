# 📚 Database Modelling & Migrations
---
A reference architecture for SE12 students using the High‑Security Flask PWA Template


This guide explains how to design, register, migrate, and manage relational database models inside the template. 
It also covers CSV import/export and RBAC‑protected CRUD operations.

The goal is to give you a **repeatable, industry‑aligned workflow** that you can use for your own projects.


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



## 4. 🔧 Creating and Running Database Migrations


## 5. 🔐 RBAC‑Protected CRUD Operations



## 6. 📥 CSV Import (Admin‑Only)



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
