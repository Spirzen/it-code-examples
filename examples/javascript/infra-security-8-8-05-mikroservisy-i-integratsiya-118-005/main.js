const amqp = require('amqplib');
async function sendMessage() {
    const connection = await amqp.connect('amqp://localhost');
    const channel = await connection.createChannel();
    // Создание очереди
    const queue = 'my_queue';
    await channel.assertQueue(queue, { durable: false });
    // Отправка сообщения
    const message = 'Hello, RabbitMQ!';
    channel.sendToQueue(queue, Buffer.from(message));
    console.log("Message sent");
    setTimeout(() => {
        connection.close();
    }, 500);
}
sendMessage();

