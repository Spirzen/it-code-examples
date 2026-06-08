# 1. Установить
pip install django

# 2. Создать проект
django-admin startproject mysite
cd mysite

# 3. Создать приложение (часть сайта)
python manage.py startapp blog

# 4. Настроить базу (по умолчанию SQLite — работает сразу)
#    Ничего трогать не надо, если SQLite подходит.

# 5. Создать таблицы в базе
python manage.py migrate

# 6. Запустить сервер для разработки
python manage.py runserver
