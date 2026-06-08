from confluent_kafka import Consumer, KafkaException

import json

class OrderConsumer:
    def __init__(self, bootstrap_servers, group_id):
        self.consumer = Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False,
            'session.timeout.ms': 30000
        })
        self.topic = 'orders'
    
    def start(self):
        self.consumer.subscribe([self.topic])
        
        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                
                if msg is None:
                    continue
                
                if msg.error():
                    raise KafkaException(msg.error())
                
                try:
                    event = json.loads(msg.value().decode('utf-8'))
                    self.process_event(event)
                    
                    # Подтверждение обработки
                    self.consumer.commit(asynchronous=False)
                    
                except json.JSONDecodeError as e:
                    print(f'Ошибка парсинга JSON: {e}')
                except Exception as e:
                    print(f'Ошибка обработки события: {e}')
                    # Можно отправить в DLQ (dead letter queue)
        
        except KeyboardInterrupt:
            print('Потребление остановлено')
        finally:
            self.consumer.close()
    
    def process_event(self, event):
        event_type = event.get('type')
        
        if event_type == 'OrderCreated':
            print(f"Создан заказ: {event['order_id']}")
            # Логика обработки...
        elif event_type == 'OrderCompleted':
            print(f"Завершён заказ: {event['order_id']}")
        else:
            print(f"Неизвестный тип события: {event_type}")

# Использование
consumer = OrderConsumer('localhost:9092', 'order-processing-group')
consumer.start()
