// Создание кнопки в интерфейсе страницы
const button = document.createElement('button');
button.textContent = 'Сохранить выделение';
button.style.position = 'fixed';
button.style.bottom = '20px';
button.style.right = '20px';
button.style.zIndex = '10000';
document.body.appendChild(button);

button.addEventListener('click', async () => {
  const selection = window.getSelection().toString().trim();
  if (selection) {
    // Отправка данных в фоновый модуль
    const response = await chrome.runtime.sendMessage({
      type: 'saveNote',
      content: selection
    });
    if (response.success) {
      button.textContent = '✓ Сохранено';
      setTimeout(() => button.textContent = 'Сохранить выделение', 1500);
    }
  }
});
