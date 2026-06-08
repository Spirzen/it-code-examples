
import random
import logging

from functools import wraps

class SamplingFilter(logging.Filter):
    """Фильтр для семплирования логов по уровню и частоте."""
    
    def __init__(self, sample_rates: dict):
        super().__init__()
        self.sample_rates = sample_rates
    
    def filter(self, record):
        level_name = record.levelname
        rate = self.sample_rates.get(level_name, 1.0)
        return random.random() < rate

# Настройка — 100% ERROR, 10% INFO, 1% DEBUG
logger = logging.getLogger("api.requests")
logger.addFilter(SamplingFilter({
    "ERROR": 1.0,
    "WARNING": 1.0,
    "INFO": 0.1,
    "DEBUG": 0.01
}))
