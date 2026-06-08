const source = new EventSource('/api/notifications/stream');

source.addEventListener('open', () => {
  console.log('соединение установлено');
});

source.addEventListener('message', (event) => {
  const payload = JSON.parse(event.data);
  appendNotification(payload);
});

source.addEventListener('ping', (event) => {
  // кастомный тип: сервер шлёт "event: ping\ndata: ...\n\n"
});

source.addEventListener('error', () => {
  // браузер переподключится с задержкой (по умолчанию)
});

// при уходе со страницы:
source.close();
