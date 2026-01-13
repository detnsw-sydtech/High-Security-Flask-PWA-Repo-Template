# Blueprint Architecture Overview  
*How your Flask application stays modular and organised*

---

## What is a Blueprint?

A **blueprint** is a modular section of a Flask application.  
Each blueprint contains its own:

- routes  
- templates  
- forms  
- logic  

This keeps your project clean, organised, and easy to extend.

---

## Why use Blueprints?

Blueprints allow you to:

- separate different parts of your app  
- avoid large, messy files  
- reuse code across projects  
- add or remove features easily  
- keep your project scalable  

This is the same pattern used in professional Flask applications.

---

## The Blueprints in This Template

### **1. auth**
Handles:
- user registration  
- login  
- logout  

Includes:
- forms  
- routes  
- templates  

### **2. main**
Handles the core functionality of your project.

For the library example:
- search  
- add item  
- view item  

For other projects:
- tasks  
- products  
- issues  
- assets  

### **3. pwa**
Handles:
- offline page  
- manifest.json  
- service worker registration  

This makes your app installable and usable offline.

---

## How Blueprints Are Registered

The application factory (`src/app/__init__.py`) registers each blueprint:
```
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(main_bp)
app.register_blueprint(pwa_bp)
```

This tells Flask where each module lives.

---

## Why this structure helps students

Students can:

- explore each module independently  
- replace the main blueprint with their own project logic  
- add new blueprints (e.g., admin, api, reports)  
- understand how large applications are organised  

This structure is intentionally designed to support both beginners and advanced learners.

---

## Where to go next

Explore:

- `src/app/auth/`  
- `src/app/main/`  
- `src/app/pwa/`  
