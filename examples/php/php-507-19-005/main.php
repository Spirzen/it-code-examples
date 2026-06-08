<?php
/**
 * Генератор строк из большого лог-файла.
 * Читает файл построчно, что позволяет обрабатывать файлы размером в гигабайты.
 */
function readLogFile(string $filename): Generator {
    $handle = fopen($filename, 'r');
    
    if (!$handle) {
        throw new RuntimeException("Не удалось открыть файл: $filename");
    }

    try {
        while (($line = fgets($handle)) !== false) {
            // trim() удаляет перенос строки и пробелы по краям
            yield trim($line);
        }
    } finally {
        fclose($handle);
    }
}

// Использование генератора
foreach (readLogFile('huge_application.log') as $line) {
    // Обработка одной строки за раз
    if (str_contains($line, 'ERROR')) {
        echo "Найдена ошибка: $line\n";
        // Операция выполняется мгновенно, память не растет
    }
}
