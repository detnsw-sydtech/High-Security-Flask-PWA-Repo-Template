// Basic PWA service worker for caching static assets

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open("v1").then(cache => {
      return cache.addAll([
        "/",              // homepage
        "/offline",       // offline fallback
      ]);
    })
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match("/offline"))
  );
});
