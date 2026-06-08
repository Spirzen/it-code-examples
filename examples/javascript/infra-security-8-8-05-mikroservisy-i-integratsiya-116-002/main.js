const WebSocket = require('ws');
const http = require('http');

// HTTP сервер для обслуживания статики
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h1>WebSocket Chat</h1>');
});

// WebSocket сервер
const wss = new WebSocket.Server({ server });

// Хранилище подключений
const clients = new Map();
const rooms = new Map();

wss.on('connection', (ws, req) => {
    const clientId = generateId();
    clients.set(clientId, ws);
    
    console.log(`Новое соединение: ${clientId}`);
    
    // Обработка сообщений
    ws.on('message', (raw) => {
        try {
            const message = JSON.parse(raw.toString());
            handleClientMessage(clientId, message);
        } catch (error) {
            console.error('Ошибка обработки сообщения:', error);
        }
    });
    
    // Обработка закрытия соединения
    ws.on('close', () => {
        console.log(`Соединение закрыто: ${clientId}`);
        handleClientDisconnect(clientId);
        clients.delete(clientId);
    });
    
    // Обработка ошибок
    ws.on('error', (error) => {
        console.error(`Ошибка соединения ${clientId}:`, error);
        clients.delete(clientId);
    });
    
    // Отправка приветственного сообщения
    ws.send(JSON.stringify({
        type: 'welcome',
        clientId: clientId,
        timestamp: Date.now()
    }));
});

function handleClientMessage(clientId, message) {
    const ws = clients.get(clientId);
    if (!ws || ws.readyState !== WebSocket.OPEN) return;
    
    switch (message.type) {
        case 'join':
            joinRoom(clientId, message.room, message.username);
            break;
            
        case 'message':
            broadcastToRoom(message.room, {
                type: 'message',
                username: message.username,
                text: message.text,
                timestamp: Date.now()
            }, clientId);
            break;
            
        case 'ping':
            ws.send(JSON.stringify({ type: 'pong' }));
            break;
            
        default:
            console.warn(`Неизвестный тип сообщения: ${message.type}`);
    }
}

function joinRoom(clientId, roomName, username) {
    if (!rooms.has(roomName)) {
        rooms.set(roomName, new Set());
    }
    
    const room = rooms.get(roomName);
    room.add(clientId);
    
    // Уведомить других участников комнаты
    broadcastToRoom(roomName, {
        type: 'user_joined',
        username: username,
        clientId: clientId,
        users: Array.from(room).map(id => ({
            id: id,
            username: getUsername(id)
        }))
    });
    
    // Подтвердить присоединение
    const ws = clients.get(clientId);
    if (ws) {
        ws.send(JSON.stringify({
            type: 'joined',
            room: roomName,
            users: Array.from(room)
        }));
    }
}

function broadcastToRoom(roomName, message, excludeClientId = null) {
    const room = rooms.get(roomName);
    if (!room) return;
    
    const data = JSON.stringify(message);
    
    room.forEach(clientId => {
        if (clientId === excludeClientId) return;
        
        const ws = clients.get(clientId);
        if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send(data);
        } else {
            // Очистить мёртвые соединения
            room.delete(clientId);
        }
    });
    
    // Удалить пустую комнату
    if (room.size === 0) {
        rooms.delete(roomName);
    }
}

function handleClientDisconnect(clientId) {
    // Удалить клиента из всех комнат
    rooms.forEach((room, roomName) => {
        if (room.has(clientId)) {
            room.delete(clientId);
            broadcastToRoom(roomName, {
                type: 'user_left',
                clientId: clientId
            });
            
            if (room.size === 0) {
                rooms.delete(roomName);
            }
        }
    });
}

function generateId() {
    return Math.random().toString(36).substr(2, 9);
}

// Запуск сервера
server.listen(8080, () => {
    console.log('Сервер запущен на порту 8080');
});
