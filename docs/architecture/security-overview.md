# Security Architecture Overview  
*Understanding how your application stays safe by default*

---

## Why security matters

Every web application needs protection against:

- cross-site scripting (XSS)  
- clickjacking  
- insecure connections  
- malicious scripts  
- data leaks  

This template includes secure defaults so you can build safely from day one.

---

## Where security is handled

Security is applied in:
```
src/app/security/
```

The main file is:

- `headers.py` — defines secure HTTP headers  
- `__init__.py` — exposes the initialisation function  

---

## Key Security Features

### **1. Content Security Policy (CSP)**  
Controls which scripts, styles, and resources the browser is allowed to load.

This helps prevent XSS attacks.

### **2. HSTS (HTTP Strict Transport Security)**  
Forces the browser to use HTTPS.

### **3. Frame Protection**  
Prevents your site from being embedded in an iframe (clickjacking protection).

### **4. XSS Protection Header**  
Adds an extra layer of browser-level XSS filtering.

---

## How security is applied

The application factory calls:
```
init_security_headers(app)
```

This attaches secure headers to every response.

Students don’t need to understand every header immediately — they get safe defaults automatically.

---

## Why this matters for your project

Whether you build:

- a library catalogue  
- a ticket tracker  
- an inventory system  
- a media database  

…your app will start with strong security foundations.

---

## Where to go next

Explore:

- `src/app/security/headers.py`  
- `src/app/__init__.py`  


