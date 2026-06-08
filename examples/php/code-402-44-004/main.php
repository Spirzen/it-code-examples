<?php
// Проверка через ===
if ($value === null) {
    handleMissingValue();
}

// Функция is_null
if (is_null($value)) {
    // Альтернативный способ проверки
}

// Оператор нулевого слияния (PHP 7.0+)
$displayName = $userName ?? 'Гость';

// Функция ??= для присваивания при отсутствии значения
$settings['theme'] ??= 'light';
?>
