// 1) Все обязательны: профиль, настройки, подписка
const [profile, settings, plan] = await Promise.all([
  fetch('/api/profile').then(r => r.json()),
  fetch('/api/settings').then(r => r.json()),
  fetch('/api/plan').then(r => r.json())
]);

// 2) Первый рабочий источник
const data = await Promise.any([
  fetch('/mirror-1').then(r => r.json()),
  fetch('/mirror-2').then(r => r.json())
]);

// 3) Таймаут через race
const timeout = new Promise((_, reject) =>
  setTimeout(() => reject(new Error('Timeout')), 2000)
);
const response = await Promise.race([fetch('/api/slow'), timeout]);
