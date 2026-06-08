configuration = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "production_db",
        "user": "app_user",
        "password": "secure_password"
    },
    "cache": {
        "type": "redis",
        "host": "cache.example.com",
        "port": 6379,
        "ttl": 300
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
    }
}
