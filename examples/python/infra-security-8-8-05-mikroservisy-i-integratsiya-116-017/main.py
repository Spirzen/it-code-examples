from confluent_kafka import Producer

import json
import uuid

from datetime import datetime

class OrderProducer:
    def __init__(self, bootstrap_servers):
        self.producer = Producer({
            'bootstrap.servers': bootstrap_servers,
            'acks': 'all',
            'enable.idempotence': True
        })
        self.topic = 'orders'
    
    def delivery_report(self, err, msg):
        if err is not None:
            print(f'Ошибка доставки: {err}')
        else:
            print(f'Сообщение доставлено: {msg.topic()} [{msg.partition()}]')
    
    def produce_order_created(self, order_id, customer_id, items):
        event = {
            'type': 'OrderCreated',
            'order_id': str(order_id),
            'customer_id': customer_id,
            'items': items,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        self.producer.produce(
            topic=self.topic,
            key=str(order_id),
            value=json.dumps(event),
            callback=self.delivery_report
        )
        
        # Ожидание доставки всех сообщений
        self.producer.flush()
    
    def close(self):
        self.producer.flush()

# Использование
producer = OrderProducer('localhost:9092')
producer.produce_order_created(
    uuid.uuid4(),
    'customer_123',
    [{'product_id': 'p1', 'quantity': 2, 'price': 100.0}]
)
producer.close()
