// Создание события с данными
const loginEvent = new CustomEvent('userLogin', {
  detail: {
    username: 'admin',
    timestamp: Date.now(),
    role: 'superuser'
  }
});

// Обработка события
document.addEventListener('userLogin', (event) => {
  const { username, role } = event.detail;
  console.log(`Пользователь ${username} вошел в систему с ролью ${role}`);
  
  // Доступ к другим свойствам
  console.log(`Время события: ${event.timeStamp}`);
  console.log(`Доверено событие: ${event.isTrusted}`);
});

// Отправка события
document.dispatchEvent(loginEvent);
