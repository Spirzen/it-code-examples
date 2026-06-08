# Список контейнеров и их состояние
docker ps -a

# Проверка детальных параметров контейнера
docker inspect <container_id>

# Просмотр процессов внутри контейнера
docker top <container_id>

# Запуск команды внутри контейнера
docker exec -it <container_id> sh

# Очистка неиспользуемых ресурсов
docker system prune
