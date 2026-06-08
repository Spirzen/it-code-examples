// 1. Найти кнопку в DOM (один раз при загрузке скрипта)
const btn = document.querySelector('.share-btn');

// 2. На клик — асинхронно открыть системный диалог "Поделиться"
btn.addEventListener('click', async () => {
  try {
    await navigator.share({
      title: document.title,
      text: 'Check this out',
      url: location.href,
    });
  } catch (err) {
    // Пользователь закрыл окно — не ошибка разработки
    if (err.name !== 'AbortError') {
      console.error('Share failed:', err);
    }
  }
});
