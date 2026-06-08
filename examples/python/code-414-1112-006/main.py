def load_test_environment():
    """Загрузка тестовой конфигурации без реальных секретов"""
    
    test_config = {
        'DB_HOST': 'localhost',
        'DB_PORT': '5432',
        'DB_NAME': 'test_db',
        'DB_USER': 'test_user',
        'DB_PASSWORD': 'test_password_placeholder',  # Не настоящий пароль
        'AWS_ACCESS_KEY_ID': 'AKIAEXAMPLE',
        'AWS_SECRET_ACCESS_KEY': 'test_secret_key_placeholder',
        'JWT_SECRET': 'test_jwt_secret_for_development_only',
    }
    
    return test_config
