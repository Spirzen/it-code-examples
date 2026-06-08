<?php
$uploadDir = '/var/www/html/uploads/';
$userFilename = $_GET['file'] ?? '';

// Нормализация пути пользователя
// realpath() разрешает относительные пути и убирает ".."
$safePath = realpath($userFilename);

// Проверка того, что путь находится внутри разрешенной директории
if ($safePath === false || strpos($safePath, realpath($uploadDir)) !== 0) {
    die("Доступ запрещен: попытка выхода за пределы директорий загрузки.\n");
}

// Дополнительная фильтрация недопустимых символов в имени файла
$cleanName = basename($userFilename);
if (!preg_match('/^[a-zA-Z0-9._-]+$/', $cleanName)) {
    die("Недопустимые символы в имени файла.\n");
}

// Использование безопасного полного пути
$finalPath = $uploadDir . $cleanName;

if (is_file($finalPath)) {
    echo "Файл найден и доступен для обработки.\n";
} else {
    echo "Файл не найден.\n";
}
?>
