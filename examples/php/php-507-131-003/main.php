<?php
/**
 * Простой консольный калькулятор
 * Поддерживаемые операции: +, -, *, /
 */

echo "Консольный калькулятор\n";
echo "Введите первое число: ";
$num1 = trim(fgets(STDIN));

echo "Введите операцию (+, -, *, /): ";
$operation = trim(fgets(STDIN));

echo "Введите второе число: ";
$num2 = trim(fgets(STDIN));

$result = 0;
$isValid = true;

switch ($operation) {
    case '+':
        $result = $num1 + $num2;
        break;
    case '-':
        $result = $num1 - $num2;
        break;
    case '*':
        $result = $num1 * $num2;
        break;
    case '/':
        if ($num2 == 0) {
            echo "Ошибка: Деление на ноль невозможно.\n";
            $isValid = false;
        } else {
            $result = $num1 / $num2;
        }
        break;
    default:
        echo "Ошибка: Неверная операция.\n";
        $isValid = false;
        break;
}

if ($isValid) {
    echo "Результат: {$num1} {$operation} {$num2} = {$result}\n";
}
?>
