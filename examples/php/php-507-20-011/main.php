<?php
$mysqli = new mysqli("localhost", "user", "password", "database_name");

// Подготовка запроса
$stmt = $mysqli->prepare("INSERT INTO logs (user_id, action, timestamp) VALUES (?, ?, NOW())");

// Привязка параметров: i (integer), s (string)
$user_id = 123;
$action = "login_success";
$stmt->bind_param("is", $user_id, $action);

// Выполнение запроса
if ($stmt->execute()) {
    // Получение ID последней вставленной записи
    echo "Вставлена запись с ID: {$stmt->insert_id}\n";
    
    // Проверка количества затронутых строк
    echo "Затронуто строк: {$stmt->affected_rows}\n";
} else {
    // Обработка ошибки через свойство error
    echo "Ошибка выполнения: {$stmt->error} (код: {$stmt->errno})\n";
}

// Повторное использование запроса без повторной подготовки (метод reset)
$stmt->reset();
$user_id = 456;
$action = "logout";
$stmt->bind_param("is", $user_id, $action);
$stmt->execute();

// Освобождение ресурсов
$stmt->close();
$mysqli->close();
?>
