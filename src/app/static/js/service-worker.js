// ------------------------------------------------------------
// Service Worker for Sydney Tech Library Catalogue
// Implements: Cache-First, Network-First, Stale-While-Revalidate
// Security: No eval(), no dynamic import, no uncontrolled caching
// ------------------------------------------------------------

// Versioned caches (bump when assets change)
const STATIC_CACHE = "static-v1";
const DYNAMIC_CACHE = "dynamic-v1";

// Pre-cache essential assets (cache-first)
const STATIC_ASSETS = [
  "/",              // homepage
  "/offline",       // offline fallback
  "/static/css/main.css",
  "/static/js/main.js",
  "/static/img/icon-192.png",
  "/static/img/icon-512.png",
  "/static/version.txt"
];

// ------------------------------------------------------------
// INSTALL — Pre-cache static assets
// ------------------------------------------------------------
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then(cache => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

// ------------------------------------------------------------
// ACTIVATE — Remove old caches
// ------------------------------------------------------------
self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys
          .filter(key => key !== STATIC_CACHE && key !== DYNAMIC_CACHE)
          .map(key => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// ------------------------------------------------------------
// FETCH — Strategy router
// ------------------------------------------------------------
self.addEventListener("fetch", event => {
  const request = event.request;

  // HTML pages → Network-first
  if (request.headers.get("accept")?.includes("text/html")) {
    event.respondWith(networkFirst(request));
    return;
  }

  // Static assets → Cache-first
  if (isStaticAsset(request.url)) {
    event.respondWith(cacheFirst(request));
    return;
  }

  // Everything else → Stale-while-revalidate
  event.respondWith(staleWhileRevalidate(request));
});

// ------------------------------------------------------------
// CACHE-FIRST
// ------------------------------------------------------------
function cacheFirst(request) {
  return caches.match(request).then(cached => {
    if (cached) {
      return cached;
    }
    return fetch(request).then(response => {
      return caches.open(DYNAMIC_CACHE).then(cache => {
        cache.put(request, response.clone());
        return response;
      });
    });
  });
}

// ------------------------------------------------------------
// NETWORK-FIRST (HTML)
// ------------------------------------------------------------
function networkFirst(request) {
  return fetch(request)
    .then(response => {
      return caches.open(DYNAMIC_CACHE).then(cache => {
        cache.put(request, response.clone());
        return response;
      });
    })
    .catch(() => {
      return caches.match(request).then(cached => {
        return cached || caches.match("/offline");
      });
    });
}

// ------------------------------------------------------------
// STALE-WHILE-REVALIDATE
// ------------------------------------------------------------
function staleWhileRevalidate(request) {
  return caches.match(request).then(cached => {
    const fetchPromise = fetch(request)
      .then(response => {
        return caches.open(DYNAMIC_CACHE).then(cache => {
          cache.put(request, response.clone());
          return response;
        });
      })
      .catch(() => cached);

    return cached || fetchPromise;
  });
}

// ------------------------------------------------------------
// Helper: Identify static assets
// ------------------------------------------------------------
function isStaticAsset(url) {
  return (
    url.includes("/static/") ||
    url.endsWith(".css") ||
    url.endsWith(".js") ||
    url.endsWith(".png") ||
    url.endsWith(".jpg") ||
    url.endsWith(".jpeg") ||
    url.endsWith(".svg") ||
    url.endsWith(".ico")
  );
}
