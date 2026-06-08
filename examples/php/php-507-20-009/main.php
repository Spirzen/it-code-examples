<?php
// Создание объекта подключения
$mysqli = new mysqli("localhost", "user", "password", "database_name");

// Проверка ошибки подключения через свойства connect_errno и connect_error
if ($mysqli->connect_errno) {
    echo "Ошибка подключения: {$mysqli->connect_error} (код: {$mysqli->connect_errno})";
    exit;
}

// Установка кодировки соединения
$mysqli->set_charset("utf8mb4");

// Получение информации о сервере и клиенте
echo "Версия MySQL: {$mysqli->server_info}\n";
echo "Версия клиента: {$mysqli->client_info}\n";
echo "Хост подключения: {$mysqli->host_info}\n";

// Проверка активности соединения методом ping
if (!$mysqli->ping()) {
    echo "Соединение потеряно\n";
} else {
    echo "Соединение активно\n";
}

// Закрытие соединения
$mysqli->close();
?>
