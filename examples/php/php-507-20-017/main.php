<?php
$logFile = 'shared_log.txt';
$message = "Запись лога от " . date('Y-m-d H:i:s') . "\n";

$handle = fopen($logFile, 'ab'); // Режим 'ab' — открытие для дозаписи бинарного файла

if ($handle === false) {
    die("Не удалось открыть файл лога.\n");
}

// Установка эксклюзивной блокировки (LOCK_EX)
// Если файл занят другим процессом, выполнение приостанавливается до освобождения
if (flock($handle, LOCK_EX)) {
    fwrite($handle, $message);
    fflush($handle); // Гарантируем запись на диск
    
    // Снятие блокировки
    flock($handle, LOCK_UN);
} else {
    echo "Не удалось установить блокировку. Файл занят.\n";
}

fclose($handle);
?>
