# 📚 Database Modelling & Migrations
---
A reference architecture for SE12 students using the High‑Security Flask PWA Template


This guide explains how to design, register, migrate, and manage relational database models inside the template. 
It also covers CSV import/export and RBAC‑protected CRUD operations.
The goal is to give you a **repeatable, industry‑aligned workflow** that you can use for your own projects.


## 1. 🧱 Where Models Live




## 2. 🧱 Understanding the Existing Model Structure



## 3. 🏗 Registering Models With the Application



## 4. 🔧 Creating and Running Database Migrations


## 5. 🔐 RBAC‑Protected CRUD Operations



## 6. 📥 CSV Import (Admin‑Only)



## 7. 📤 CSV Export (Admin + Librarian)


## 8. 🖥 Building the Catalogue UI




## 9. 🔌 JSON API Endpoints (Optional but Powerful)




## 10. 🧪 Automated Testing




## 11. 🗂 Recommended Folder Structure

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




