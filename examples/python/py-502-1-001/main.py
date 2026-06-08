#!/usr/bin/env python3
"""
Модуль: hello.py
Автор: Иван Петров
Описание: Простой пример вывода сообщения.
"""

# Импорт необходимых модулей

import sys

# Определение констант
GREETING = "Привет, мир!"

# Основная логика
def main():
    print(GREETING)
    return 0

# Точка входа
if __name__ == "__main__":
    sys.exit(main())
