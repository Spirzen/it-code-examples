# 1. Создание проекта
mkdir analysis-tool
cd analysis-tool

# 2. Создание окружения
python -m venv .venv

# 3. Активация
source .venv/bin/activate  # Linux/macOS

# 4. Обновление инструментов внутри окружения
pip install --upgrade pip setuptools wheel

# 5. Установка зависимостей
pip install pandas numpy matplotlib requests

# 6. Фиксация зависимостей
pip freeze > requirements.txt

# 7. Работа с проектом
python main.py

# 8. Деактивация
deactivate

# 9. Удаление окружения при необходимости
rm -rf .venv
