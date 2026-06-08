<?php
// Пример чтения содержимого файла целиком
$fileContent = file_get_contents('data.txt');

if ($fileContent === false) {
    // Обработка ошибки чтения
    error_log("Не удалось прочитать файл data.txt");
    exit;
}

echo "Содержимое файла:\n";
echo $fileContent;

// Пример записи данных в файл (перезапись существующего)
$newData = "Новая строка данных\n";
$bytesWritten = file_put_contents('data.txt', $newData);

if ($bytesWritten !== false) {
    echo "\nУспешно записано {$bytesWritten} байт.\n";
} else {
    echo "Ошибка при записи в файл.\n";
}

// Пример добавления данных в конец файла без перезаписи
$appendData = "Добавленная строка\n";
file_put_contents('data.txt', $appendData, FILE_APPEND | LOCK_EX);
?>
