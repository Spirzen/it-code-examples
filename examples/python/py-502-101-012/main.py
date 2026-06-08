from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    database_url: str = Field(
        default="postgresql://localhost:5432/myapp",
        description="URL подключения к базе данных"
    )
    redis_url: str = Field(
        default="redis://localhost:6379/0",
        description="URL подключения к Redis"
    )
    debug: bool = Field(
        default=False,
        description="Режим отладки"
    )
    secret_key: str = Field(
        default="insecure-default-key-for-dev",
        description="Секретный ключ для подписи токенов"
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
