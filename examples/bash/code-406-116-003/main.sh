# Начало бисекции — текущий коммит сломан, предыдущий работал
git bisect start
git bisect bad HEAD
git bisect good HEAD~10

# Git переключается на промежуточный коммит
# Проверяем сборку
dotnet build

# Сообщаем результат Git
git bisect good  # или git bisect bad

# Повторяем до нахождения первого сломанного коммита
