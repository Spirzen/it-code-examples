# 1. Установка зависимостей
sudo apt update && sudo apt install -y \
  openjdk-17-jre-headless \
  curl wget gnupg \
  systemd-journal-remote

# 2. Проверка Java
java -version
# Должно — openjdk version "17.0.12" 2024-07-16

# 3. Создание пользователя
sudo useradd --Система --home /opt/orion --shell /bin/false orion
sudo mkdir -p /opt/orion/{Данные,logs,config}
sudo chown -R orion:orion /opt/orion
