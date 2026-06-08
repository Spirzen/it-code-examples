
import pytest

from pydantic import ValidationError

class TestAppConfig:
    """Тесты валидации конфигурации."""
    
    def test_valid_configuration(self, monkeypatch):
        """Валидная конфигурация загружается успешно."""
        monkeypatch.setenv("ENVIRONMENT", "development")
        monkeypatch.setenv("SERVICE_VERSION", "1.2.3")
        monkeypatch.setenv("DB_HOST", "localhost")
        monkeypatch.setenv("DB_NAME", "myapp_test")
        monkeypatch.setenv("DB_USERNAME", "testuser")
        monkeypatch.setenv("DB_PASSWORD", "testpassword")
        monkeypatch.setenv("REDIS_URL", "redis://localhost:6379/1")
        monkeypatch.setenv(
            "SECURITY_JWT_SECRET",
            "a" * 64  # Достаточно длинный секрет
        )
        
        config = AppConfig()
        assert config.environment == Environment.DEVELOPMENT
        assert config.database.host == "localhost"
    
    def test_production_requires_strong_jwt_secret(self, monkeypatch):
        """Production требует криптостойкий JWT-секрет."""
        monkeypatch.setenv("ENVIRONMENT", "production")
        monkeypatch.setenv("SERVICE_VERSION", "1.2.3")
        monkeypatch.setenv("DB_HOST", "db.prod.internal")
        monkeypatch.setenv("DB_NAME", "myapp")
        monkeypatch.setenv("DB_USERNAME", "app")
        monkeypatch.setenv("DB_PASSWORD", "prodpassword")
        monkeypatch.setenv("REDIS_URL", "redis://cache.internal:6379/0")
        monkeypatch.setenv("SECURITY_JWT_SECRET", "weak")
        
        with pytest.raises(ValidationError) as exc_info:
            AppConfig()
        
        errors = exc_info.value.errors()
        assert any(
            "уникальных символов" in str(e['msg'])
            for e in errors
        )
    
    def test_production_forbids_debug_logging(self, monkeypatch):
        """Production запрещает DEBUG-логирование."""
        monkeypatch.setenv("ENVIRONMENT", "production")
        monkeypatch.setenv("LOG_LEVEL", "debug")
        monkeypatch.setenv("SERVICE_VERSION", "1.2.3")
        monkeypatch.setenv("DB_HOST", "db.prod.internal")
        monkeypatch.setenv("DB_NAME", "myapp")
        monkeypatch.setenv("DB_USERNAME", "app")
        monkeypatch.setenv("DB_PASSWORD", "prodpassword")
        monkeypatch.setenv("REDIS_URL", "redis://cache.internal:6379/0")
        monkeypatch.setenv(
            "SECURITY_JWT_SECRET",
            "a" * 64
        )
        
        with pytest.raises(ValidationError) as exc_info:
            AppConfig()
        
        errors = exc_info.value.errors()
        assert any("DEBUG" in str(e['msg']) for e in errors)
    
    def test_database_pool_limits(self, monkeypatch):
        """Размер пула БД ограничен разумными пределами."""
        monkeypatch.setenv("DB_POOL_SIZE", "1000")  # Слишком много
        
        with pytest.raises(ValidationError) as exc_info:
            DatabaseSettings(
                host="localhost",
                name="test",
                username="test",
                password="test"
            )
        
        errors = exc_info.value.errors()
        assert any("pool_size" in str(e['loc']) for e in errors)
