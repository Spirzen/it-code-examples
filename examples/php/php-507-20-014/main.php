<?php
$mysqli = new mysqli("localhost", "user", "password", "database_name");

// Подготовка запроса для получения данных
$stmt = $mysqli->prepare("SELECT id, name, email, created_at FROM users LIMIT 5");
$stmt->execute();

// Получение результата в виде объекта mysqli_result (если доступно расширение mysqlnd)
$result = $stmt->get_result();

if ($result) {
    // Получение метаданных всех полей
    $fields = $result->fetch_fields();
    foreach ($fields as $field) {
        echo "Поле: {$field->name}, Тип: {$field->type}, Длина: {$field->length}\n";
    }

    // Извлечение строки в виде объекта
    while ($row = $result->fetch_object()) {
        echo "Объект: ID={$row->id}, Email={$row->email}\n";
    }

    // Перемещение указателя (data_seek)
    $result->data_seek(2); // Переход к третьей строке
    $row = $result->fetch_assoc();
    echo "Строка после seek: {$row['name']}\n";

    // Освобождение результата
    $result->free_result();
}

$stmt->close();
$mysqli->close();
?>
