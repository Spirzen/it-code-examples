const { Kafka } = require('kafkajs');

const kafka = new Kafka({
    clientId: 'order-service',
    brokers: ['localhost:9092']
});

const producer = kafka.producer({
    acks: -1, // all replicas
    idempotent: true
});

async function produceOrderCreated(orderId, customerId, items) {
    await producer.connect();
    
    const event = {
        type: 'OrderCreated',
        orderId: orderId,
        customerId: customerId,
        items: items,
        timestamp: new Date().toISOString()
    };
    
    await producer.send({
        topic: 'orders',
        messages: [{
            key: orderId,
            value: JSON.stringify(event)
        }]
    });
    
    console.log(`Событие отправлено: ${orderId}`);
    await producer.disconnect();
}

// Использование
produceOrderCreated(
    'order-123',
    'customer-456',
    [{ productId: 'p1', quantity: 2, price: 100 }]
).catch(console.error);
