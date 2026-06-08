
import hvac
import os

from dataclasses import dataclass
from typing import Optional

@dataclass
class DatabaseCredentials:
    host: str
    port: int
    username: str
    password: str
    database: str
    
    @property
    def url(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class SecretManager:
    """Менеджер секретов на базе HashiCorp Vault."""
    
    def __init__(self):
        self.client = hvac.Client(
            url=os.environ.get('VAULT_ADDR', 'http://localhost:8200'),
            token=os.environ.get('VAULT_TOKEN'),
        )
        
        # Аутентификация через Kubernetes ServiceAccount
        if os.environ.get('KUBERNETES_SERVICE_HOST'):
            self._authenticate_kubernetes()
        
        self.environment = os.environ.get('ENVIRONMENT', 'development')
        self.mount_point = os.environ.get('VAULT_MOUNT', 'secret')
    
    def _authenticate_kubernetes(self):
        """Аутентификация через Kubernetes JWT."""
        with open('/var/run/secrets/kubernetes.io/serviceaccount/token') as f:
            jwt = f.read()
        
        self.client.auth.kubernetes.login(
            role=os.environ.get('VAULT_ROLE', 'myapp'),
            jwt=jwt,
        )
    
    def get_database_credentials(self) -> DatabaseCredentials:
        """Получение учётных данных базы данных."""
        path = f"production/database/main"
        
        secret = self.client.secrets.kv.v2.read_secret_version(
            path=path,
            mount_point=self.mount_point,
        )
        
        data = secret['data']['data']
        
        return DatabaseCredentials(
            host=data['host'],
            port=int(data['port']),
            username=data['username'],
            password=data['password'],
            database=data['database'],
        )
    
    def get_api_key(self, service: str) -> str:
        """Получение API-ключа внешнего сервиса."""
        path = f"{self.environment}/services/{service}"
        
        secret = self.client.secrets.kv.v2.read_secret_version(
            path=path,
            mount_point=self.mount_point,
        )
        
        return secret['data']['data']['api_key']
    
    def get_tls_certificate(self, domain: str) -> dict:
        """Получение TLS-сертификата и приватного ключа."""
        path = f"certificates/{domain}"
        
        secret = self.client.secrets.kv.v2.read_secret_version(
            path=path,
            mount_point=self.mount_point,
        )
        
        return {
            'certificate': secret['data']['data']['certificate'],
            'private_key': secret['data']['data']['private_key'],
            'ca_chain': secret['data']['data']['ca_chain'],
        }
