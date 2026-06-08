<?php
/**
 * Конвертер форматов дат
 * Использование: php date_converter.php <дата> <формат_ввода> <формат_вывода>
 */

$dateString = $argv[1] ?? '';
$inputFormat = $argv[2] ?? 'Y-m-d';
$outputFormat = $argv[3] ?? 'd.m.Y';

if (empty($dateString)) {
    die("Укажите дату\n");
}

$timestamp = strtotime($dateString);

if ($timestamp === false) {
    die("Ошибка: Невалидный формат даты\n");
}

$formattedDate = date($outputFormat, $timestamp);

echo "Ввод: {$dateString} ({$inputFormat})\n";
echo "Вывод: {$formattedDate} ({$outputFormat})\n";
?>
