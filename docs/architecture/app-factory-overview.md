# Application Factory Overview  

*Understanding how your Flask app is created and organised*

---

## What is the Application Factory?

In modern Flask applications, the app is not created at the top level of the program.  
Instead, it is created inside a function called an **application factory**.

This pattern makes your project:

- easier to test  
- easier to configure  
- easier to extend  
- more professional  
- more modular  

The factory lives in:
```bash
src/app/init.py
```


Whenever Flask needs to run your project, it calls this function to build the app.

---

## Why do we use an Application Factory?

### 1. It keeps the project modular  
Different parts of the app (auth, search, PWA, etc.) live in separate folders called **blueprints**.  
The factory brings them together.

### 2. It supports database migrations  
The factory initialises SQLAlchemy and Alembic so you can create and update your database structure safely.

### 3. It supports testing  
You can create multiple app instances with different configurations (e.g., testing, development, production).

### 4. It keeps configuration in one place  
Database settings, security settings, and other configuration values are all loaded here.

### 5. It is the recommended pattern for real‑world Flask applications  
This is how professional Flask systems are built.

---

## What does the Application Factory do?

The factory performs several important tasks:

### **1. Creates the Flask app**
This is the core object that represents your web application.

### **2. Loads configuration**
This includes:
- the secret key  
- the database connection  
- SQLAlchemy settings  

These can be changed depending on the environment.

### **3. Initialises the database**
The factory connects SQLAlchemy to the app and sets up Alembic migrations.

This allows you to:
- define models  
- run `flask db migrate`  
- run `flask db upgrade`  

### **4. Registers blueprints**
Blueprints are modular sections of the app.  
In this template, we have:

- `auth` — login, logout, registration  
- `main` — search, add item, view item  
- `pwa` — offline support and manifest  

Each blueprint has its own routes, forms, and templates.

### **5. Applies security headers**
The factory calls a helper function that adds secure HTTP headers to every response.

This includes:
- Content Security Policy  
- HSTS  
- Frame protection  
- XSS protection  

You get secure defaults without needing to understand every header immediately.

### **6. Returns the fully configured app**
At the end, the factory returns the complete Flask application object.

This is what Flask uses to:
- run the development server  
- run tests  
- serve the app in production  

---

## Why this matters for your project

This template is designed so you can build **any** relational Flask project.

The application factory makes it easy to:

- add new blueprints  
- add new models  
- change the database  
- add new features  
- keep your project organised  

Whether you are building:
- a library catalogue  
- an inventory system  
- a ticket tracker  
- a media database  
- a project management tool  

…the same structure works.

---

## Where to go next

After understanding the application factory, explore:

- `src/app/db/models.py` — the relational database models  
- `src/app/auth/` — user registration and login  
- `src/app/main/` — search, add item, view item  
- `src/app/pwa/` — offline support  
- `src/app/security/` — secure HTTP headers  

Each module builds on the foundation created by the application factory.

---

If you have questions or want to customise your project, talk to your teacher or explore the documentation in the `docs/architecture` folder.


--8<-- "../_includes/footer.md"
