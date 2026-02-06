# Progressive Web App (PWA) Architecture

This document explains the architecture of the Progressive Web App (PWA) used in this project.
It is written for senior Software Engineering students (Stage 6) who are expected to understand:

- Web application architecture
- Client–server interactions
- Caching strategies
- Secure coding practices
- Deployment considerations

The PWA implemented in this system follows industry‑standard patterns and is intentionally designed to be readable, auditable, and extensible.

## Overview of a PWA

A Progressive Web App is a web application enhanced with capabilities traditionally associated with native applications. These capabilities include:

- Offline operation
- Installability
- Background updates
- Local caching for performance
- A consistent user experience across devices

PWAs rely on three core components:
1. Service Worker – a background script that intercepts network requests and manages caching.
2. Web App Manifest – metadata describing how the app behaves when installed.
3. HTTPS – required for security and to enable service worker functionality.

This project implements all three components in a secure and standards‑compliant manner.

## 2. Architectural Model

```table
+-----------------------------------------------------------+
|                         Browser                           |
+-----------------------------------------------------------+
|  HTML  |  CSS  |  JS  |  Images  |  API Requests          |
+-----------------------------------------------------------+
                 ↑                     |
                 |                     ↓
+-----------------------------------------------------------+
|                     Service Worker                        |
|  - Intercepts fetch requests                             |
|  - Applies caching strategies                            |
|  - Provides offline fallback                             |
+-----------------------------------------------------------+
                 ↑                     |
                 |                     ↓
+-----------------------------------------------------------+
|                           Caches                          |
|  STATIC_CACHE   (pre-cached assets)                       |
|  DYNAMIC_CACHE  (runtime caching)                         |
+-----------------------------------------------------------+

```


## 3. Caching Strategies Implemented

The service worker uses three complementary caching strategies. These mirror patterns used in production PWAs such as Google Workspace, GitHub Mobile, and Twitter Lite.

### 3.1 Cache‑First

**Use case:**
- Static assets that rarely change (CSS, JS bundles, icons, images).

**Behaviour:**
- Return the cached version immediately.
- If not cached, fetch from the network and store it.

**Advantages:**
- Extremely fast load times.
- Reduces network usage.

**Trade‑offs:**
- Requires explicit versioning to avoid stale assets.

### 3.2 Network‑First

**Use case:**
- Dynamic or user‑specific data where freshness is critical (API responses, user profiles, dashboards).

**Behaviour:**
- Attempt to fetch a fresh response from the network first.
- If the network request fails or times out, fall back to a cached response (if available).
- Optionally cache successful network responses for future offline use.

**Advantages:**
- Ensures users see the most up‑to‑date data when online.
- Provides a reasonable offline experience by falling back to cached data.

**Trade‑offs:**
- Slower than cache‑first when network latency is high.
- Behaviour depends on network availability; must be tuned with appropriate timeouts.

### 3.3 Stale‑While‑Revalidate

**Use case:**
- Content that benefits from being very fast but should still eventually reflect updates (CDN‑backed images, font files, configuration JSON, semi‑static pages).

**Behaviour:**
- Return the cached response immediately if present (“stale”).
- In parallel, fetch an updated response from the network.
- When the network response arrives, update the cache for the next request.

**Advantages:**
- Combines fast perceived performance with eventual consistency.
- Hides network latency on repeat visits.

**Trade‑offs:**
- Users may briefly see outdated content until the background update completes.
- Requires careful versioning and cache invalidation to avoid long‑lived stale data in critical flows.
