# Подход с наследованием
class NotificationService:
    def send(self, user, message):
        raise NotImplementedError()

class EmailNotificationService(NotificationService):
    def send(self, user, message):
        send_email(user.email, message)

class SMSNotificationService(NotificationService):
    def send(self, user, message):
        send_sms(user.phone, message)

class UserNotifier:
    def __init__(self, notification_service):
        self.notification_service = notification_service
    
    def notify_user(self, user, message):
        self.notification_service.send(user, message)

# Подход с композицией
class EmailSender:
    def send(self, recipient, message):
        send_email(recipient, message)

class SMSSender:
    def send(self, recipient, message):
        send_sms(recipient, message)

class UserNotifier:
    def __init__(self, email_sender, sms_sender):
        self.email_sender = email_sender
        self.sms_sender = sms_sender
    
    def notify_by_email(self, user, message):
        self.email_sender.send(user.email, message)
    
    def notify_by_sms(self, user, message):
        self.sms_sender.send(user.phone, message)
