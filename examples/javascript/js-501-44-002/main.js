const btn = document.querySelector('.share-btn');
if (!btn) return;

btn.addEventListener('click', async () => {
  const payload = {
    title: document.title,
    text: 'Посмотри эту статью',
    url: location.href,
  };

  if (navigator.share) {
    try {
      await navigator.share(payload);
    } catch (err) {
      if (err.name !== 'AbortError') console.error(err);
    }
    return;
  }

  // Запасной путь: десктоп без Web Share — копируем URL
  try {
    await navigator.clipboard.writeText(payload.url);
    alert('Ссылка скопирована в буфер обмена');
  } catch {
    prompt('Скопируйте ссылку:', payload.url);
  }
});
