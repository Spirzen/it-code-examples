from fastapi import FastAPI, HTTPException
from typing import Dict

import logging

app = FastAPI()
logger_registry: Dict[str, logging.Logger] = {}

@app.get("/admin/logging/levels")
async def get_logging_levels():
    """Получение текущих уровней всех логгеров."""
    return {
        name: logging.getLevelName(logger.level)
        for name, logger in logger_registry.items()
    }

@app.put("/admin/logging/levels/{logger_name}")
async def set_logging_level(logger_name: str, level: str):
    """Изменение уровня логирования без перезапуска."""
    target_logger = logging.getLogger(logger_name)
    
    numeric_level = getattr(logging, level.upper(), None)
    if numeric_level is None:
        raise HTTPException(400, f"Некорректный уровень: {level}")
    
    old_level = logging.getLevelName(target_logger.level)
    target_logger.setLevel(numeric_level)
    
    logger_registry[logger_name] = target_logger
    
    return {
        "logger": logger_name,
        "old_level": old_level,
        "new_level": level
    }
