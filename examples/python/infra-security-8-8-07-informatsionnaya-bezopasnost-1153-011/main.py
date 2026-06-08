class DynamicDatabaseCredentials:
    """Динамические учётные данные для PostgreSQL через Vault."""
    
    def __init__(self, vault_client: SecretManager):
        self.vault = vault_client
    
    def get_credentials(self, role: str = "readonly") -> dict:
        """Получение временных учётных данных."""
        # Vault создаёт нового пользователя PostgreSQL
        # с правами только на чтение и TTL 1 час
        response = self.vault.client.secrets.database.generate_credentials(
            name=role,
            mount_point='database',
        )
        
        return {
            'username': response['data']['username'],
            'password': response['data']['password'],
            'lease_id': response['lease_id'],
            'lease_duration': response['lease_duration'],
        }
    
    def renew_lease(self, lease_id: str, increment: int = 3600):
        """Продление времени жизни учётных данных."""
        self.vault.client.sys.renew_lease(
            lease_id=lease_id,
            increment=increment,
        )
    
    def revoke_lease(self, lease_id: str):
        """Досрочный отзыв учётных данных."""
        self.vault.client.sys.revoke_lease(lease_id=lease_id)
