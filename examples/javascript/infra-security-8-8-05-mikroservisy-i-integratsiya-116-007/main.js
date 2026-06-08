// Создание соединения
const eventSource = new EventSource('https://api.example.com/stream', {
    withCredentials: true // Для передачи cookies
});

// Обработчик всех событий (тип по умолчанию 'message')
eventSource.onmessage = (event) => {
    console.log('Получено сообщение:', event.data);
};

// Обработчик события с типом 'notification'
eventSource.addEventListener('notification', (event) => {
    const data = JSON.parse(event.data);
    console.log('Уведомление:', data);
    showNotification(data.title, data.body);
});

// Обработчик события с типом 'progress'
eventSource.addEventListener('progress', (event) => {
    const data = JSON.parse(event.data);
    updateProgressBar(data.percent);
});

// Обработчик ошибок
eventSource.onerror = (error) => {
    console.error('Ошибка SSE:', error);
    
    // Проверка состояния соединения
    switch (eventSource.readyState) {
        case EventSource.CONNECTING:
            console.log('Переподключение...');
            break;
        case EventSource.CLOSED:
            console.log('Соединение закрыто');
            // Можно создать новое соединение
            break;
    }
};

// Получение последнего ID события
console.log('Последнее событие ID:', eventSource.lastEventId);

// Закрытие соединения
function closeConnection() {
    eventSource.close();
    console.log('Соединение закрыто вручную');
}

// Пример использования с обработкой различных типов событий
const handlers = {
    'message': (payload) => console.log('Сообщение:', payload),
    'update': (payload) => updateUI(payload),
    'error': (payload) => showError(payload),
    'complete': (payload) => {
        console.log('Завершено:', payload);
        eventSource.close();
    }
};

Object.entries(handlers).forEach(([type, handler]) => {
    eventSource.addEventListener(type, (event) => {
        try {
            const data = JSON.parse(event.data);
            handler(data);
        } catch (e) {
            console.error('Ошибка парсинга JSON:', e);
        }
    });
});
