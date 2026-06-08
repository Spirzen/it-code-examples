const controller = new AbortController();
const { signal } = controller;

const request = fetch('/api/search?q=js', { signal })
  .then((response) => response.json())
  .then((data) => renderResults(data))
  .catch((error) => {
    if (error.name === 'AbortError') {
      return; // ожидаемая отмена, не ошибка UX
    }
    showError(error);
  });

// пользователь набрал новый запрос:
controller.abort();
