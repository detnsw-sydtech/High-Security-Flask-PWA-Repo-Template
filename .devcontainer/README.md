```markdown
# 📘 High‑Security Flask PWA — Devcontainer Guide

## 🧩 Purpose of this folder
The `.devcontainer/` directory defines the **entire development environment** for this project.  
When a Codespace is created, this folder ensures:

- the correct Python version (3.12)
- a reproducible virtual environment
- consistent dependency installation
- automatic Flask startup
- safe, predictable automation
- identical behaviour for every student and staff member

This guarantees a stable, secure, and fully reproducible environment.

---

## 📁 Folder structure

### Root files
- **devcontainer.json**  
  Defines the container image, automation commands, ports, and VS Code extensions.

- **preflight.sh**  
  Safety checks that run *synchronously* on every Codespace start.  
  Validates Python version, uv installation, and venv drift.

- **startup.sh**  
  Automation that runs *asynchronously* after preflight.  
  Creates `.venv` if missing, activates it, runs `uv sync`, and launches Flask.

### Subdirectories
- **scripts/**  
  Optional helper scripts for staff and advanced debugging.  
  Not executed automatically.

- **logs/**  
  Documentation about runtime logs (not actual logs).

---

## 🚀 What happens when the Codespace starts

### **1. Container builds**
- Uses Python 3.12 (Debian Bullseye base image)
- Installs VS Code extensions
- Sets up port forwarding

### **2. `preflight.sh` runs**
- Checks system Python version
- Checks uv installation
- Detects virtual environment drift
- Prints warnings but does not modify anything

### **3. `startup.sh` runs**
- Ensures `.venv` exists (creates it if missing)
- Activates the virtual environment
- Runs `uv sync` to install/update dependencies
- Launches Flask automatically in the background
- Logs output to `/tmp/startup.log` and `/tmp/flask.log`

Students do not need to run anything manually.

---

## 🧪 Rebuilding the Codespace

If something seems out of sync:

1. Open the Command Palette  
2. Run **Dev Containers: Rebuild Container**  
3. Wait for Flask to auto‑launch

If the container fails to build:

- delete the Codespace  
- create a new one from GitHub  
- everything will rebuild automatically

This guarantees a clean environment.

---

## 📝 Logs

Runtime logs are stored in the container’s temporary filesystem:

- `/tmp/startup.log` — output from the startup script  
- `/tmp/flask.log` — Flask server output

These files are **not** committed to the repository.

---

## 🛠️ Staff‑only helper scripts

Inside `.devcontainer/scripts/`:

- **install-uv.sh**  
  Reinstalls uv safely.

- **rebuild-venv.sh**  
  Deletes `.venv`, recreates it, and runs `uv sync`.

- **diagnostics.sh**  
  Prints environment details (Python, uv, venv, ports, Flask status).

Students do not need these scripts during normal operation.

---

## 🧼 Resetting the environment

If the environment becomes inconsistent:

1. Delete the Codespace  
2. Create a new Codespace on `main`  
3. Everything will rebuild automatically

This is the fastest and most reliable recovery method.

---

## 🎓 For students

You do **not** need to:

- install Python
- install uv
- create a virtual environment
- run `uv sync`
- start Flask manually

Everything is automated.

Your job is to:

- write code
- test your app
- commit your work
- push to GitHub

The environment takes care of the rest.

---

## 🛡️ For staff

This devcontainer is designed to be:

- reproducible
- audit‑ready
- stable across cohorts
- resistant to drift
- easy to repair

If a student’s environment breaks:

- run `diagnostics.sh`
- or rebuild the Codespace
- or reset the venv with `rebuild-venv.sh`

If the devcontainer itself breaks:

- repair `devcontainer.json` on a clean branch
- delete all Codespaces
- recreate a fresh Codespace on `main`

```

```tree
.devcontainer/
│
├── devcontainer.json
│   # Canonical configuration:
│   # - Python 3.12 base image
│   # - overrideCommand: false
│   # - postStartCommand runs preflight + startup
│   # - port forwarding + VS Code extensions
│
├── preflight.sh
│   # Layer 1 automation:
│   # - Validates Python version
│   # - Checks uv installation
│   # - Detects venv drift
│   # - Never mutates the environment
│   # - Safe to run synchronously on every boot
│
├── startup.sh
│   # Layer 2 automation:
│   # - Ensures .venv exists (creates if missing)
│   # - Activates venv
│   # - Runs uv sync
│   # - Launches Flask in background
│   # - Writes logs to /tmp/startup.log
│
├── scripts/
│   ├── install-uv.sh
│   │   # Optional helper:
│   │   # - Installs uv if missing
│   │   # - Used only in postCreateCommand (if ever needed)
│   │
│   ├── rebuild-venv.sh
│   │   # Optional helper:
│   │   # - rm -rf .venv && uv venv && uv sync
│   │   # - Used for drift recovery or teaching moments
│   │
│   └── diagnostics.sh
│       # Optional helper:
│       # - Prints environment diagnostics
│       # - Useful for student debugging
│
├── logs/
│   └── README.md
│       # Explains:
│       # - /tmp/startup.log (Flask + startup output)
│       # - /tmp/flask.log (Flask runtime logs)
│       # - Why logs are not stored in the repo
│
└── README.md
    # Student‑facing documentation:
    # - What the devcontainer does
    # - How automation works
    # - How to rebuild the Codespace
    # - How to interpret preflight warnings
    # - How to read startup logs
```
