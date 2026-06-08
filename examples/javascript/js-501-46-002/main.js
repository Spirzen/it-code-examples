self.addEventListener('push', (event) => {
  const data = event.data?.json() ?? { title: 'Новое событие' };

  event.waitUntil(
    self.registration.showNotification(data.title, {
      body: data.body ?? 'Откройте приложение, чтобы посмотреть детали',
      icon: '/logo.png',
      data: { url: data.url ?? '/' },
    })
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const target = event.notification.data?.url ?? '/';
  event.waitUntil(clients.openWindow(target));
});
