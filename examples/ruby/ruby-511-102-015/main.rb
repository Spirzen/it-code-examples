class Notification
  def send
    raise NotImplementedError, "Метод должен быть переопределен"
  end
end

class EmailNotification < Notification
  def initialize(email, subject, body)
    @email = email
    @subject = subject
    @body = body
  end
  
  def send
    "Отправка письма на #{@email}: #{@subject}"
  end
end

class SMSNotification < Notification
  def initialize(phone, message)
    @phone = phone
    @message = message
  end
  
  def send
    "Отправка SMS на #{@phone}: #{@message[0..50]}"
  end
end

class PushNotification < Notification
  def initialize(device_token, title, content)
    @device_token = device_token
    @title = title
    @content = content
  end
  
  def send
    "Отправка push на устройство #{@device_token}: #{@title}"
  end
end

class SlackNotification < Notification
  def initialize(webhook_url, channel, text)
    @webhook_url = webhook_url
    @channel = channel
    @text = text
  end
  
  def send
    "Отправка в Slack канал #{@channel}: #{@text[0..30]}"
  end
end

notifications = [
  EmailNotification.new("user@example.com", "Добро пожаловать", "Спасибо за регистрацию..."),
  SMSNotification.new("+79001234567", "Ваш код подтверждения: 123456"),
  PushNotification.new("abc123def456", "Новое сообщение", "У вас новое сообщение..."),
  SlackNotification.new("https://hooks.slack.com/...", "#general", "Важное объявление...")
]

notifications.each do |notification|
  puts notification.send
end

# Отправка письма на user@example.com — Добро пожаловать
# Отправка SMS на +79001234567 — Ваш код подтверждения: 123456
# Отправка push на устройство abc123def456 — Новое сообщение
# Отправка в Slack канал #general — Важное объявление...
