<?php
$filename = 'large_log.txt';
$handle = fopen($filename, 'r+');

if ($handle === false) {
    die("Не удалось открыть файл для чтения и записи.\n");
}

// Чтение первой строки
$firstLine = fgets($handle);
if ($firstLine !== false) {
    echo "Первая строка: " . trim($firstLine) . "\n";
}

// Перемещение указателя чтения к началу файла
rewind($handle);

// Запись новой строки в начало файла
fwrite($handle, "Запись в начало файла\n");

// Сброс буфера записи, чтобы данные гарантированно попали на диск
fflush($handle);

// Явное закрытие ресурса
fclose($handle);

echo "Операции завершены успешно.\n";
?>
