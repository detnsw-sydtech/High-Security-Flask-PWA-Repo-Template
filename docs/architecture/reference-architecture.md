# Reference architecture for the Online Library Catalogue

This document describes the high-level architecture of the STHS Flask PWA
Online Library Catalogue. It is designed to help students and staff see how
the different parts of the application fit together:

- blueprints (modular route groups)
- database models
- API endpoints
- PWA components
- security and diagnostics

---

## 1. High-level components

At a high level, the application consists of:

- **Flask application factory** (`src/app/__init__.py`)
- **Blueprints** for different concerns:
  - `main` — public pages and core UI
  - `auth` — login/logout flow
  - `pwa` — manifest, service worker, offline page
  - `security` — diagnostics and security headers
  - `api` — JSON endpoints for catalogue data
- **Database layer** (`src/app/db/`) using SQLAlchemy models
- **Static assets** (CSS, JS, icons) and **templates** (HTML)

Each blueprint is responsible for a specific part of the system and is
registered in the application factory.

---

## 2. Blueprint responsibilities

### `main` blueprint (`src/app/main/`)

- Serves the main landing page (`/`)
- Provides basic informational and health endpoints:
  - `/health`
  - `/info`
- Renders HTML templates (e.g. `index.html`)
- Acts as the “front door” of the application

### `auth` blueprint (`src/app/auth/`)

- Handles authentication flow:
  - `/login` (GET/POST)
  - `/logout`
- Currently uses placeholder logic to demonstrate:
  - form handling
  - redirects
  - blueprint organisation
- Can later be extended to use real users and sessions

### `pwa` blueprint (`src/app/pwa/`)

- Serves PWA-related assets:
  - `/pwa/manifest.json`
  - `/pwa/service-worker.js`
  - `/pwa/offline`
- Supports installation of the app as a Progressive Web App
- Provides a `/pwa/health` endpoint for monitoring and DAST

### `security` blueprint (`src/app/security/`)

- Provides operational and security diagnostics:
  - `/security/health`
  - `/security/headers`
  - `/security/info`
- Demonstrates recommended security headers
- Helps students understand how to expose safe diagnostic endpoints

### `api` blueprint (`src/app/api/`)

- Exposes JSON endpoints for the Online Library Catalogue:
  - `GET /api/items` — list items with pagination and optional search
  - `GET /api/items/<id>` — retrieve a single item
  - `GET /api/categories` — list categories
  - `GET /api/creators` — list creators
  - `GET /api/item-types` — list item types
  - `GET /api/search` — convenience search endpoint
- Reads real data from the database using SQLAlchemy models
- Designed for:
  - frontend integrations (HTMX, fetch, etc.)
  - future mobile/PWA offline sync
  - security scanning (DAST tools like Wapiti)

---

## 3. Data layer (SQLAlchemy models)

The data layer lives in `src/app/db/` and consists of:

- `db/__init__.py` — defines the global `db = SQLAlchemy()` instance
- `db/models.py` — defines ORM models:

  - `Role` — user roles (e.g. member, staff, admin)
  - `User` — application users
  - `ItemType` — types of items (Book, Video, etc.)
  - `Item` — catalogue items
  - `Creator` — authors, artists, etc.
  - `Category` — genres, tags, subjects

Relationships include:

- one-to-many:
  - `Role → User`
  - `ItemType → Item`
- many-to-many:
  - `Item ↔ Creator`
  - `Item ↔ Category`

The API blueprint queries these models and serialises them into JSON.

---

## 4. How the pieces connect

The application factory (`src/app/__init__.py`) is responsible for:

- creating the Flask app instance
- initialising extensions (e.g. `db.init_app(app)`)
- registering blueprints in a dependency-safe order:
  - `main` (core pages)
  - `auth` (depends on `main` for redirects)
  - `pwa`
  - `security`
  - `api`

The flow looks like this:

```mermaid
flowchart TD

    subgraph Client
        Browser["Browser / PWA shell"]
    end

    subgraph FlaskApp["Flask Application (src/app)"]
        MainBP["main blueprint\nHTML pages\n/ /health /info"]
        AuthBP["auth blueprint\n/login /logout"]
        PWABP["pwa blueprint\n/pwa/manifest.json\n/pwa/service-worker.js\n/pwa/offline"]
        SecBP["security blueprint\n/security/health\n/security/headers\n/security/info"]
        ApiBP["api blueprint\n/api/items\n/api/search\n/api/categories"]
    end

    subgraph DataLayer["Data Layer (src/app/db)"]
        Models["SQLAlchemy models\nItem, User, Role,\nCreator, Category, ItemType"]
        DB["Database (e.g. SQLite/PostgreSQL)"]
    end

    Browser --> MainBP
    Browser --> AuthBP
    Browser --> PWABP
    Browser --> SecBP
    Browser --> ApiBP

    ApiBP --> Models
    MainBP --> Models

    Models --> DB
