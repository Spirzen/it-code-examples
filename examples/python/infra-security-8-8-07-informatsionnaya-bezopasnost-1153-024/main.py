from fastapi import FastAPI

import logging

app = FastAPI()
logger = logging.getLogger(__name__)

# Инициализация наблюдателя
config_watcher = ConsulConfigWatcher(
    host="consul.internal",
    prefix="myapp/production/config/"
)

# Реакция на изменение уровня логирования
def on_log_level_change(key: str, old_value: Any, new_value: Any):
    """Обновление уровня логирования при изменении конфигурации."""
    if key == "log_level":
        numeric_level = getattr(logging, new_value.upper(), logging.INFO)
        logging.getLogger().setLevel(numeric_level)
        logger.info(f"Уровень логирования изменён: {old_value} -> {new_value}")

# Реакция на изменение лимитов
def on_rate_limit_change(key: str, old_value: Any, new_value: Any):
    """Обновление лимитов запросов."""
    if key == "rate_limit_per_minute":
        rate_limiter.update_limit(new_value)
        logger.info(f"Лимит запросов изменён: {old_value} -> {new_value}")

# Регистрация наблюдателей
config_watcher.watch("log_level", on_log_level_change)
config_watcher.watch("rate_limit_per_minute", on_rate_limit_change)

@app.on_event("startup")
async def startup():
    config_watcher.start()

@app.on_event("shutdown")
async def shutdown():
    config_watcher.stop()
