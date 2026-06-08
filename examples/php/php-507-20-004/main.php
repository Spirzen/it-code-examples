<?php
$mysqli = new mysqli("localhost", "root", "", "test_db");

$name = "Иван Петров";
$email = "ivan@example.com";
$age = 25;

// Подготовка запроса
$stmt = $mysqli->prepare("INSERT INTO users (name, email, age) VALUES (?, ?, ?)");
$stmt->bind_param("ssi", $name, $email, $age); // s=string, i=integer

if ($stmt->execute()) {
    $user_id = $stmt->insert_id; // Получаем ID новой записи
    echo "Пользователь добавлен! ID: " . $user_id;
} else {
    echo "Ошибка: " . $stmt->error;
}

$stmt->close();
?>
