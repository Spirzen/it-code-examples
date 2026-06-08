class LamportClock:
    def __init__(self):
        self.time = 0
    
    def tick(self):
        """Локальное событие."""
        self.time += 1
        return self.time
    
    def send(self):
        """Отправка сообщения."""
        self.time += 1
        return self.time
    
    def receive(self, message_time):
        """Получение сообщения."""
        self.time = max(self.time, message_time) + 1
        return self.time
