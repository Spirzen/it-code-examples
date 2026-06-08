# Клонирование репозитория
git clone https://sourcecraft.dev/project/repo.git

# Добавление удалённого источника
git remote add origin https://sourcecraft.dev/user/project.git

# Создание новой ветки
git checkout -b feature/new-feature

# Коммит изменений
git add src/file.py
git commit -m "Добавление новой функциональности обработки данных"

# Пушинг в удалённый репозиторий
git push origin feature/new-feature
