
import time

from email.utils import formataddr
from typing import List, Dict, Tuple

def send_bulk_emails(
    recipients: List[Dict[str, str]],  # [{'name': '...', 'email': '...'}, ...]
    subject: str,
    text_template: str,
    html_template: str | None = None,
    smtp_config: Dict[str, str] = None
) -> Tuple[int, List[str]]:
    """
    Отправляет персонализированные письма списку получателей.
    Возвращает (успешно_отправлено, список_ошибок).
    """
    successes = 0
    errors = []

    with smtplib.SMTP(smtp_config['host'], smtp_config['port']) as server:
        server.starttls()
        server.login(smtp_config['user'], smtp_config['password'])

        for rec in recipients:
            try:
                # Формируем письмо для конкретного получателя
                msg = MIMEMultipart('alternative')
                msg['From'] = formataddr(('Вселенная IT', smtp_config['from_email']))
                msg['To'] = formataddr((rec['name'], rec['email']))
                msg['Subject'] = subject

                text = text_template.format(name=rec['name'])
                msg.attach(MIMEText(text, 'plain', 'utf-8'))

                if html_template:
                    html = html_template.format(name=rec['name'])
                    msg.attach(MIMEText(html, 'html', 'utf-8'))

                server.send_message(msg)
                successes += 1

                # Пауза между письмами (например, 1 сек — 3600 писем/час)
                time.sleep(smtp_config.get('delay', 1.0))

            except smtplib.SMTPRecipientsRefused as e:
                # Постоянная ошибка для этого получателя — фиксируем и идём дальше
                errors.append(f"{rec['email']}: {e.smtp_code} {e.recipients}")
            except smtplib.SMTPServerDisconnected:
                # Сервер разорвал соединение — переподключаемся
                server.connect(smtp_config['host'], smtp_config['port'])
                server.starttls()
                server.login(smtp_config['user'], smtp_config['password'])
                # Повторяем попытку для этого получателя (можно добавить счётчик)
            except Exception as e:
                errors.append(f"{rec['email']}: {type(e).__name__}: {e}")

    return successes, errors
