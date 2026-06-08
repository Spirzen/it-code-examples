
import boto3

from botocore.exceptions import ClientError

import json

from functools import lru_cache

class AWSSecretManager:
    """Менеджер секретов на базе AWS Secrets Manager."""
    
    def __init__(self, region_name: str = "eu-west-1"):
        self.client = boto3.client(
            service_name='secretsmanager',
            region_name=region_name,
        )
        self.environment = os.environ.get('ENVIRONMENT', 'development')
    
    @lru_cache(maxsize=100)
    def get_secret(self, secret_name: str) -> dict:
        """Получение секрета с кэшированием."""
        full_name = f"{self.environment}/{secret_name}"
        
        try:
            response = self.client.get_secret_value(SecretId=full_name)
            
            if 'SecretString' in response:
                return json.loads(response['SecretString'])
            else:
                # Бинарный секрет
                return response['SecretBinary']
                
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'DecryptionFailure':
                raise RuntimeError("Не удалось расшифровать секрет")
            elif error_code == 'ResourceNotFoundException':
                raise RuntimeError(f"Секрет {full_name} не найден")
            else:
                raise
    
    def get_database_url(self) -> str:
        """Получение строки подключения к БД."""
        secret = self.get_secret("database/main")
        return (
            f"postgresql://{secret['username']}:{secret['password']}"
            f"@{secret['host']}:{secret['port']}/{secret['database']}"
        )
    
    def rotate_secret(self, secret_name: str):
        """Инициирование ротации секрета."""
        full_name = f"{self.environment}/{secret_name}"
        self.client.rotate_secret(SecretId=full_name)
