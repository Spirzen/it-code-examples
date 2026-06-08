<?php
$mysqli = new mysqli("localhost", "user", "password", "database_name");

$input_string = "O'Reilly's \"Quote\"";

// Экранирование специальных символов
$safe_string = $mysqli->real_escape_string($input_string);

// Формирование запроса (не рекомендуется для новых проектов, но показано для полноты)
$query = "SELECT * FROM quotes WHERE author = '{$safe_string}'";

// Выполнение запроса
$result = $mysqli->query($query);

if ($result) {
    echo "Запрос выполнен успешно.\n";
    $mysqli->free_result($result);
} else {
    echo "Ошибка: {$mysqli->error}\n";
}

$mysqli->close();
?>
