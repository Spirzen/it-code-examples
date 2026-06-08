<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $subject = $_POST['subject'] ?? '';
    $message = trim($_POST['message'] ?? '');

    // Валидация
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        die('Все поля обязательны.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Некорректный email.');
    }

    if (!in_array($subject, ['support', 'suggestion', 'complaint', 'other'])) {
        die('Недопустимая тема.');
    }

    // Здесь должна быть отправка письма или сохранение в БД
    // Пример:
    // mail('admin@example.com', "Обратная связь: $subject", $message, "From: $email");

    echo '<p style="color: green; text-align: center;">Сообщение успешно отправлено!</p>';
}
?>
