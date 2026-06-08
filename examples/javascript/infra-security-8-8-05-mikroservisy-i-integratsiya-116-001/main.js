// Создание соединения
const ws = new WebSocket('wss://example.com/chat');

// Обработчики событий
ws.addEventListener('open', (event) => {
    console.log('Соединение установлено');
    // Отправка сообщения после установки соединения
    ws.send(JSON.stringify({
        type: 'join',
        room: 'general',
        username: 'Тимур'
    }));
});

ws.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    console.log('Получено сообщение:', data);
    
    switch (data.type) {
        case 'message':
            displayMessage(data.username, data.text);
            break;
        case 'user_joined':
            updateUserList(data.users);
            break;
    }
});

ws.addEventListener('error', (event) => {
    console.error('Ошибка соединения:', event);
});

ws.addEventListener('close', (event) => {
    console.log('Соединение закрыто:', event.code, event.reason);
    // Автоматическое переподключение
    setTimeout(() => reconnect(), 3000);
});

// Отправка сообщения
function sendMessage(text) {
    if (ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({
            type: 'message',
            text: text,
            timestamp: Date.now()
        }));
    }
}

// Проверка активности
let pingInterval = setInterval(() => {
    if (ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({ type: 'ping' }));
    }
}, 30000);

ws.addEventListener('close', () => {
    clearInterval(pingInterval);
});
