# Установка Django (если еще не установлен)
pip install django

# Создание виртуального окружения (рекомендуется)
python -m venv venv

# Активация виртуального окружения
# Для Windows —
venv\Scripts\activate
# Для macOS/Linux —
source venv/bin/activate

# Создание нового проекта
django-admin startproject my_first_django_project
cd my_first_django_project

# Запуск сервера разработки
python manage.py runserver
