# Удаляем мёртвый код
git rm dead-code.cs

# Фиксируем изменение с описанием
git commit -m "Удалён неиспользуемый класс LegacyProcessor"

# При необходимости код можно восстановить из истории
git log --all --full-history -- "**/LegacyProcessor.cs"
git checkout <commit-hash> -- path/to/LegacyProcessor.cs
