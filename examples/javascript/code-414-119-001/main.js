// Регистрация прослушивателя клика по иконке
chrome.action.onClicked.addListener((tab) => {
  // Выполнение скрипта на активной вкладке
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => {
      alert('Расширение активировано!');
    }
  });
});

// Обработка сообщений от контентных скриптов
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === 'getSettings') {
    chrome.storage.local.get(['theme', 'language'], (Данные) => {
      sendResponse({ settings: Данные });
    });
    return true; // сохранить канал для асинхронного ответа
  }
});
