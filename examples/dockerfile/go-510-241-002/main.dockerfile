# Этап сборки
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Копирование файлов модуля
COPY go.mod ./
RUN go mod download

# Копирование исходного кода
COPY . .

# Сборка приложения
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# Этап запуска
FROM alpine:latest

WORKDIR /root/

# Копирование скомпилированного бинарника
COPY --from=builder /app/main .

# Открытие порта
EXPOSE 8080

# Команда запуска
CMD ["./main"]
