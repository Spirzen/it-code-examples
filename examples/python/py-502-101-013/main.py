from abc import ABC, abstractmethod
from typing import List

class EmailService(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        pass

class SESMailService(EmailService):
    def __init__(self, aws_region: str):
        self.client = boto3.client("ses", region_name=aws_region)
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        try:
            self.client.send_email(
                Source="noreply@example.com",
                Destination={"ToAddresses": [to]},
                Message={
                    "Subject": {"Данные": subject},
                    "Body": {"Text": {"Данные": body}}
                }
            )
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {to}: {e}")
            return False

class DebugEmailService(EmailService):
    def send_email(self, to: str, subject: str, body: str) -> bool:
        logger.debug(f"DEBUG EMAIL to {to}\nSubject: {subject}\n\n{body}")
        return True
