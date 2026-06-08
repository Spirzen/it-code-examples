<?php
/**
 * Генератор надежных паролей
 * 
 * Параметры:
 * - длина пароля (по умолчанию 16)
 * - включение цифр (true по умолчанию)
 * - включение спецсимволов (true по умолчанию)
 */

function generatePassword(int $length = 16, bool $useDigits = true, bool $useSpecial = true): string {
    // Определение наборов символов
    $lowercase = 'abcdefghijklmnopqrstuvwxyz';
    $uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $digits = '0123456789';
    $special = '!@#$%^&*()_+-=[]{}|;:,.<>?';

    $characterSet = $lowercase . $uppercase;

    if ($useDigits) {
        $characterSet .= $digits;
    }

    if ($useSpecial) {
        $characterSet .= $special;
    }

    $maxLength = strlen($characterSet);
    $password = '';

    for ($i = 0; $i < $length; $i++) {
        // Генерация безопасного случайного индекса
        $index = random_int(0, $maxLength - 1);
        $password .= $characterSet[$index];
    }

    return $password;
}

// Пример использования
echo "Сгенерированный пароль: " . generatePassword(20, true, true) . PHP_EOL;
echo "Пароль без спецсимволов: " . generatePassword(12, true, false) . PHP_EOL;
?>
