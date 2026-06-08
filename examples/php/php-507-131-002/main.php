<?php
/**
 * Сортировка строк из текстового файла
 * 
 * Использование: php sort_file.php input.txt output_sorted.txt
 */

if ($argc < 2) {
    die("Использование: php sort_file.php <input_file> [output_file]\n");
}

$inputFile = $argv[1];

if (!file_exists($inputFile)) {
    die("Ошибка: Файл не найден: {$inputFile}\n");
}

// Чтение всех строк файла в массив
$lines = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

if (empty($lines)) {
    echo "Файл пуст или не содержит данных.\n";
    exit(0);
}

// Сортировка массива по алфавиту (режим сортировки: естественный порядок)
sort($lines, SORT_STRING | SORT_FLAG_CASE);

// Определение выходного файла
$outputFile = $argc > 2 ? $argv[2] : null;

if ($outputFile) {
    // Запись отсортированных строк в новый файл
    $result = implode(PHP_EOL, $lines) . PHP_EOL;
    file_put_contents($outputFile, $result);
    echo "Данные успешно сохранены в: {$outputFile}\n";
} else {
    // Вывод в консоль
    foreach ($lines as $line) {
        echo $line . PHP_EOL;
    }
}
?>
