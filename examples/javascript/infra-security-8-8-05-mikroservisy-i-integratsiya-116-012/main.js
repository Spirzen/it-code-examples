const express = require('express');
const app = express();

/**
 * Простой SSE поток
 */
app.get('/events', (req, res) => {
    // Установка заголовков
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');
    res.setHeader('X-Accel-Buffering', 'no'); // Отключение буферизации nginx
    
    // Получение последнего события
    const lastEventId = req.headers['last-event-id'];
    let eventId = lastEventId ? parseInt(lastEventId) : 0;
    
    console.log(`Клиент подключился, последнее событие: ${lastEventId || 'нет'}`);
    
    // Отправка начального события
    sendEvent(res, 'connected', { message: 'Подключено к потоку' }, ++eventId);
    
    // Установка интервала повтора
    res.write(`retry: 5000\n\n`);
    
    // Генерация событий
    const interval = setInterval(() => {
        if (res.writableEnded) {
            clearInterval(interval);
            console.log('Клиент отключился');
            return;
        }
        
        const data = {
            id: ++eventId,
            timestamp: Date.now(),
            message: `Событие #${eventId}`
        };
        
        sendEvent(res, 'tick', data, eventId.toString());
        
        // Отправка комментария
        res.write(`: Серверное время ${new Date().toISOString()}\n\n`);
        res.flush();
        
    }, 2000);
    
    // Обработка отключения
    req.on('close', () => {
        clearInterval(interval);
        console.log('Соединение закрыто клиентом');
    });
    
    // Обработка ошибок
    res.on('error', (err) => {
        clearInterval(interval);
        console.error('Ошибка потока:', err);
    });
});

/**
 * Поток уведомлений
 */
const notifications = [];
let notificationId = 0;

app.get('/notifications', (req, res) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');
    
    const lastEventId = req.headers['last-event-id'];
    let lastId = lastEventId ? parseInt(lastEventId) : 0;
    
    console.log(`Уведомления: восстановление с #${lastId}`);
    
    // Отправка накопленных уведомлений
    notifications
        .filter(n => n.id > lastId)
        .forEach(notification => {
            sendEvent(res, 'notification', notification.data, notification.id.toString());
        });
    
    // Отслеживание новых уведомлений
    const checkInterval = setInterval(() => {
        if (res.writableEnded) {
            clearInterval(checkInterval);
            return;
        }
        
        const newNotifications = notifications.filter(n => n.id > lastId);
        
        newNotifications.forEach(notification => {
            sendEvent(res, 'notification', notification.data, notification.id.toString());
            lastId = notification.id;
        });
        
        if (newNotifications.length > 0) {
            res.flush();
        }
        
    }, 1000);
    
    req.on('close', () => {
        clearInterval(checkInterval);
    });
});

/**
 * Создание уведомления
 */
app.post('/notify', express.json(), (req, res) => {
    notificationId++;
    
    const notification = {
        id: notificationId,
        data: {
            type: req.body.type || 'info',
            title: req.body.title || 'Уведомление',
            body: req.body.body || '',
            timestamp: Date.now()
        }
    };
    
    notifications.push(notification);
    
    console.log(`Новое уведомление #${notificationId}:`, notification.data);
    
    res.json({ status: 'created', id: notificationId });
});

/**
 * Вспомогательная функция отправки события
 */
function sendEvent(res, eventType, data, id = null) {
    if (id) {
        res.write(`id: ${id}\n`);
    }
    
    if (eventType !== 'message') {
        res.write(`event: ${eventType}\n`);
    }
    
    const dataStr = typeof data === 'string' ? data : JSON.stringify(data);
    dataStr.split('\n').forEach(line => {
        res.write(`data: ${line}\n`);
    });
    
    res.write('\n'); // Пустая строка завершает событие
}

// Запуск сервера
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Сервер запущен на порту ${PORT}`);
});
