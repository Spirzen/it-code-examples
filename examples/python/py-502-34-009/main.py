
import logging
import traceback

from typing import Optional

# Конфигурация — из переменных окружения
SMTP_CONFIG = {
    'host': os.getenv('SMTP_HOST'),
    'port': int(os.getenv('SMTP_PORT', 587)),
    'user': os.getenv('SMTP_USER'),
    'password': os.getenv('SMTP_PASSWORD'),
    'from_email': os.getenv('ALERT_FROM_EMAIL')
}

TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = int(os.getenv('ADMIN_TELEGRAM_CHAT_ID'))

class AlertHandler(logging.Handler):
    """Кастомный лог-хендлер для отправки критических ошибок."""
    
    def emit(self, record: logging.LogRecord):
        if record.levelno < logging.ERROR:
            return

        # Формируем текст уведомления
        error_summary = f"КРИТИЧЕСКАЯ ОШИБКА в {record.module}:{record.funcName}\n"
        error_summary += f"Уровень: {record.levelname}\n"
        error_summary += f"Сообщение: {record.getMessage()}\n"

        if record.exc_info:
            error_summary += "\nТрассировка:\n"
            error_summary += ''.join(traceback.format_exception(*record.exc_info))[-1000:]  # последние 1000 символов

        # Отправка в Telegram (асинхронно, но в sync-контексте — через asyncio.run)
        try:
            asyncio.run(
                send_telegram_alert(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, 
                                   f"<b>🚨 Авария</b>\n<pre>{error_summary[:4000]}</pre>")
            )
        except Exception as e:
            # Если Telegram недоступен — fallback на email
            self._send_email_fallback(error_summary)

    def _send_email_fallback(self, body: str):
        try:
            msg = MIMEMultipart()
            msg['From'] = SMTP_CONFIG['from_email']
            msg['To'] = os.getenv('ADMIN_EMAIL')
            msg['Subject'] = '[CRITICAL] Ошибка в Вселенной IT'
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            with smtplib.SMTP(SMTP_CONFIG['host'], SMTP_CONFIG['port']) as server:
                server.starttls()
                server.login(SMTP_CONFIG['user'], SMTP_CONFIG['password'])
                server.send_message(msg)
        except Exception as e_mail:
            # Крайний fallback — запись в stderr
            print(f"ПОЛНЫЙ ОТКАЗ СИСТЕМЫ ОПОВЕЩЕНИЙ: {e_mail}", file=sys.stderr)
