
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Подготовка сообщения
msg = MIMEMultipart()
msg['From'] = 'sender@gmail.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Тестовое письмо из Вселенной IT'

body = 'Это простое текстовое сообщение.'
msg.attach(MIMEText(body, 'plain', 'utf-8'))

# Соединение и отправка
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()          # Включение шифрования
        server.login('sender@gmail.com', 'app_password_here')
        server.send_message(msg)
except smtplib.SMTPException as e:
    print(f'Ошибка SMTP: {e}')
