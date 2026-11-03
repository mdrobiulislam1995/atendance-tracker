self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('ajwa-store').then((cache) => {
      return cache.addAll([
        '/',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'
      ]);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});
