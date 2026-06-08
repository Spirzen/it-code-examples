
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Приложение запущено")

try:
    result = 10 / 2
    logging.debug("Промежуточный результат: %s", result)
except ZeroDivisionError:
    logging.exception("Ошибка деления на ноль")

logging.warning("Свободная память на сервере меньше 20%")
