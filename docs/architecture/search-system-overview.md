# Search System Overview  
*How searching works in your relational Flask application*

---

## Why search matters

Most applications need a way to find information quickly.

Examples:
- find a book  
- find a product  
- find a task  
- find a document  

This template includes a flexible search system that works with any relational data.

---

## Where search is implemented

Search lives in:

```
src/app/main/
```

Key files:
- `forms.py` — defines the search form  
- `queries.py` — reusable search functions  
- `routes.py` — handles search requests  
- `templates/main/search.html` — search page  
- `templates/main/results.html` — results page  

---

## How the search form works

The search form allows users to filter by:

- keyword  
- item type  
- category  
- creator  
- year  

Students can add more filters depending on their project.

---

## How the search query works

The search system uses SQLAlchemy to build queries dynamically.

A typical search might:

- join Item → ItemType  
- join Item → Creator  
- join Item → Category  
- filter by keyword  
- filter by type  
- filter by category  
- filter by creator  

This teaches students how relational queries work in real applications.

---

## Role-Based Search Restrictions

Some fields may be visible only to certain users.

Examples:
- members cannot search internal notes  
- staff can  
- admins can search everything  

This is called:

- **Role-Based Access Control (RBAC)**  
- **Attribute-Based Access Control (ABAC)** for field-level restrictions  

The search system supports both.

---

## Why this system is flexible

Students can reuse the search system for:

- tasks  
- products  
- issues  
- assets  
- documents  
- media  

The structure stays the same — only the meaning changes.

---

## Where to go next

Explore:

- `src/app/main/forms.py`  
- `src/app/main/queries.py`  
- `src/app/main/routes.py`  
