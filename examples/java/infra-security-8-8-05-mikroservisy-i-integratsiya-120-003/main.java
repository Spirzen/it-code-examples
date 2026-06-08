// Подписка на очередь с обработкой push-событий
Channel channel = connection.createChannel();
channel.queueDeclare("notifications", true, false, false, null);
channel.basicQos(1); // fair dispatch

DeliverCallback deliverCallback = (consumerTag, delivery) -> {
    try {
        String message = new String(delivery.getBody(), StandardCharsets.UTF_8);
        processNotification(message);
        channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
    } catch (Exception e) {
        // Возврат в очередь с ограничением попыток через DLX
        channel.basicNack(delivery.getEnvelope().getDeliveryTag(), false, false);
    }
};

channel.basicConsume("notifications", false, deliverCallback, consumerTag -> {});
