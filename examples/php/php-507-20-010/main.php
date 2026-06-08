<?php
$mysqli = new mysqli("localhost", "user", "password", "database_name");

// Выполнение SQL-запроса
$result = $mysqli->query("SELECT id, name FROM users WHERE active = 1");

if (!$result) {
    // Обработка ошибки через свойство error_list
    foreach ($mysqli->error_list as $error) {
        echo "Ошибка: {$error['message']} (SQLSTATE: {$error['sqlstate']})\n";
    }
    exit;
}

// Получение количества полей в результате
echo "Количество столбцов: {$result->field_count}\n";

// Перебор строк в виде ассоциативного массива
while ($row = $result->fetch_assoc()) {
    echo "ID: {$row['id']}, Имя: {$row['name']}\n";
}

// Освобождение памяти
$result->free_result();

// Пример использования свойства affected_rows для UPDATE запроса
$updateResult = $mysqli->query("UPDATE users SET status = 'new' WHERE active = 0");
if ($updateResult) {
    echo "Изменено строк: {$mysqli->affected_rows}\n";
}

$mysqli->close();
?>
