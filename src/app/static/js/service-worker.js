// Minimal service worker script. This file must contain valid JavaScript.

self.addEventListener('install', function (event) {
    // No-op install handler; immediately activate the new service worker.
    self.skipWaiting();
});

self.addEventListener('activate', function (event) {
    // Take control of uncontrolled clients as soon as possible.
    event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', function (event) {
    // Pass-through fetch handler; let the network handle all requests.
    return;
});
