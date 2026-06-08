const form = document.getElementById('signup');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  const body = new FormData(form);
  // Дополнительные поля, которых нет в HTML:
  body.append('source', 'web');

  const response = await fetch('/api/signup', {
    method: 'POST',
    body, // Content-Type с boundary выставит браузер сам
  });

  if (!response.ok) throw new Error('Ошибка сервера');
  const data = await response.json();
  console.log('Создан пользователь', data.id);
});
