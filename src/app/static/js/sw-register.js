// Service worker registration (CSP-safe, no inline)
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/static/js/service-worker.js')
      .catch((err) => {
        // Optionally log to a monitoring endpoint
        console.error('Service worker registration failed', err);
      });
  });
}
