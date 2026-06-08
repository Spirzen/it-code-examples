const { Kafka } = require('kafkajs');

const kafka = new Kafka({
    clientId: 'order-processor',
    brokers: ['localhost:9092']
});

const consumer = kafka.consumer({
    groupId: 'order-processing-group',
    sessionTimeout: 30000
});

async function startConsumer() {
    await consumer.connect();
    await consumer.subscribe({ topic: 'orders', fromBeginning: true });
    
    await consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
            try {
                const event = JSON.parse(message.value.toString());
                console.log(`Получено событие: ${event.type}`);
                
                await processEvent(event);
                
                // Смещение автоматически подтверждается
            } catch (error) {
                console.error('Ошибка обработки:', error);
                // Можно отправить в DLQ
            }
        }
    });
}

async function processEvent(event) {
    switch (event.type) {
        case 'OrderCreated':
            console.log(`Создан заказ: ${event.orderId}`);
            // Логика обработки...
            break;
        case 'OrderCompleted':
            console.log(`Завершён заказ: ${event.orderId}`);
            break;
        default:
            console.log(`Неизвестный тип: ${event.type}`);
    }
}

// Запуск
startConsumer().catch(console.error);

// Graceful shutdown
process.on('SIGTERM', async () => {
    await consumer.disconnect();
    process.exit(0);
});
