const button = document.querySelector('#notify-btn');
if (!button) throw new Error('Кнопка #notify-btn не найдена');

button.addEventListener('click', async () => {
  if (!('Notification' in window)) {
    alert('Notification API не поддерживается');
    return;
  }

  let permission = Notification.permission;
  if (permission === 'default') {
    permission = await Notification.requestPermission();
  }

  if (permission !== 'granted') {
    alert('Разрешение на уведомления не выдано');
    return;
  }

  const notification = new Notification('Hey! 👋', {
    body: 'Ваш отчет готов к скачиванию.',
    icon: '/logo.png',
    tag: 'report-ready',
  });

  notification.onclick = () => {
    window.focus();
    location.href = '/reports/latest';
  };
});
