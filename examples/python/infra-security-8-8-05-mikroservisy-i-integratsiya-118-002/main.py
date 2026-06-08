def callback(ch, method, properties, body):
    try:
        process(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception:
        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=False  # отправка в DLX при настройке
        )

channel.basic_qos(prefetch_count=3)
channel.basic_consume(
    queue='Задачи',
    on_message_callback=callback,
    auto_ack=False
)
channel.start_consuming()
