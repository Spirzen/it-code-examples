# Python - выводится трассировка и завершение

import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    print(f"Критическая ошибка: {exc_value}")
    # Логирование

sys.excepthook = handle_exception
