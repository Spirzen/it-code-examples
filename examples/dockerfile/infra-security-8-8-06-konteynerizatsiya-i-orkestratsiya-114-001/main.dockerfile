# Базовый образ
FROM node:16-alpine

# Создание рабочей директории
WORKDIR /app

# Копирование package.json и установка зависимостей
COPY package*.json ./
RUN npm install

# Копирование исходного кода
COPY . .

# Команда для запуска приложения
CMD ["node", "index.js"]

