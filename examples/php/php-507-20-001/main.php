<?php
// Подключение
$mysqli = new mysqli("localhost", "username", "password", "database_name");

// Проверка ошибок
if ($mysqli->connect_error) {
    die("Ошибка подключения: " . $mysqli->connect_error);
}

echo "Успешно подключено!";

// Установка кодировки (важно для русского языка)
$mysqli->set_charset("utf8mb4");
?>
