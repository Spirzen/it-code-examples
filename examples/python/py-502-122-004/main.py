
import os
import sys

# 1. Получение текущей рабочей директории
current_dir = os.getcwd()
print(f"Текущая директория: {current_dir}")

# 2. Работа с путями (кроссплатформенно)
# Вместо использования слешей '/' или '\\', используем os.path.join
path_to_file = os.path.join(current_dir, "Данные", "report.txt")
print(f"Полный путь к файлу: {path_to_file}")

# Проверка существования пути
if os.path.exists(path_to_file):
    print("Файл существует.")
else:
    # Создание директории, если её нет
    os.makedirs(os.path.dirname(path_to_file), exist_ok=True)
    print(f"Директория создана: {os.path.dirname(path_to_file)}")

# 3. Переменные окружения
user_home = os.environ.get('HOME') or os.environ.get('USERPROFILE')
print(f"Домашняя папка пользователя: {user_home}")

# 4. Список файлов в директории
try:
    files = os.listdir(current_dir)
    print(f"Файлы в директории: {files[:5]}...") # Показываем первые 5
except PermissionError:
    print("Нет доступа к чтению директории.")

# 5. Удаление файла (если он существует)
# if os.path.exists(path_to_file) —
#     os.remove(path_to_file)
