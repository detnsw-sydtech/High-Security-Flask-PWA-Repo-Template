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

```text
+-----------------------------------------------------------+
|                         Browser                           |
+-----------------------------------------------------------+
|  HTML  |  CSS  |  JS  |  Images  |  API Requests          |
+-----------------------------------------------------------+
                 ↑                     |
                 |                     ↓
+-----------------------------------------------------------+
|                     Service Worker                        |
|  - Intercepts fetch requests                               |
|  - Applies caching strategies                              |
|  - Provides offline fallback                               |
+-----------------------------------------------------------+
                 ↑                     |
                 |                     ↓
+-----------------------------------------------------------+
|                           Caches                          |
|  STATIC_CACHE   (pre-cached assets)                       |
|  DYNAMIC_CACHE  (runtime caching)                         |
+-----------------------------------------------------------+

```




