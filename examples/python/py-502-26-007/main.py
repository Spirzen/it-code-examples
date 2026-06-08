class DatabaseConnection:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
    
    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict['host'],
            config_dict['port'],
            config_dict['user'],
            config_dict['password']
        )

conn = DatabaseConnection.from_config({
    'host': 'localhost',
    'port': 5432,
    'user': 'admin',
    'password': 'secret'
})
