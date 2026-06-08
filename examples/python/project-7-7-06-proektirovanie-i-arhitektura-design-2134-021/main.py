
import hvac
import os

class SecretManager:
    def __init__(self):
        self.client = hvac.Client(
            url=os.environ['VAULT_ADDR'],
            token=os.environ['VAULT_TOKEN']
        )
        self.environment = os.environ['ENVIRONMENT']
    
    def get_database_credentials(self) -> dict:
        """Получение учётных данных БД из Vault."""
        secret = self.client.secrets.kv.v2.read_secret_version(
            path=f'production/database/{self.environment}',
            mount_point='secret'
        )
        return secret['data']['data']
    
    def get_api_keys(self, service: str) -> dict:
        """Получение API-ключей внешнего сервиса."""
        secret = self.client.secrets.kv.v2.read_secret_version(
            path=f'services/{service}/{self.environment}',
            mount_point='secret'
        )
        return secret['data']['data']
