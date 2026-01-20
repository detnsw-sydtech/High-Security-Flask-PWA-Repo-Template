[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/detnsw-sydtech/High-Security-Flask-PWA-Repo-Template?quickstart=1)

# High‑Security Flask PWA — Reference Architecture (SE12)

This repository is the official **detnsw‑sydtech** high‑security Flask Progressive Web App template for **Year 12 Software Engineering (SE12)** students.  
It provides a **modern, secure, reproducible Python environment** and a **reference architecture** suitable for Major Projects, assessments, and real‑world software engineering practice.

---

## 🚀 What this template provides

### Modern Python Toolchain
- Uses `pyproject.toml` for clean dependency management  
- Powered by **uv** for fast installs and reproducible environments  
- Automatic virtual environment creation  
- Deterministic builds using `uv.lock`

### High‑Security Flask Architecture
- Secure‑by‑default Flask structure  
- Modular blueprints  
- Layered security patterns  
- Clear separation of concerns  
- Ready for authentication, authorisation, and secure data handling

### Progressive Web App (PWA) Support
- Web App Manifest  
- Service Worker  
- Offline caching  
- Installable app behaviour  
- Modern front‑end structure

### Automated CI Pipeline
- Linting and formatting  
- Automated testing  
- **Wapiti dynamic security scanning (DAST)**  
- GitHub Actions workflow for reproducible builds

### SE12 Reference Architecture
This repository models:
- professional project structure  
- reproducible development environments  
- secure coding practices  
- automated tooling  
- documentation and governance patterns  

Students can use this as:
- a starting point for Major Projects  
- a reference for secure Flask development  
- a guide to modern Python tooling  
- a template for reproducible workflows

---

## 🧩 Development Environment (GitHub Codespaces)

This repo includes a **fully automated devcontainer** that handles:

1. Creating a virtual environment (`.venv`)  
2. Installing dependencies using `uv sync`  
3. Launching the Flask development server  
4. Opening the project with all required VS Code extensions  

Nothing needs to be installed locally — everything runs in the cloud.

For details, see:  
`/.devcontainer/README.md`

---

## 🏗️ Creating Your Project Structure

To scaffold the full project layout:

1. Open the **Actions** tab  
2. Run the workflow **“Build repository structure”**  
3. The project structure will be generated automatically

**Actions**
This ensures every student begins with the same secure, consistent architecture.

## 📚 Documentation
Full documentation is being built out and will include:

Flask architecture overview
PWA behaviour and offline caching
Security patterns
CI/CD pipeline explanation
Devcontainer automation flow

## Student and staff troubleshooting guides

### 🎓 For Students
You do not need to:
- install Python
- install uv
- create a virtual environment
- run uv sync
- start Flask manually

**Everything is automated.**

Your job is to:
- write code
- test your app
- commit your work
- push to GitHub

The environment takes care of the rest.
