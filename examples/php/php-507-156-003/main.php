<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'] ?? '';
    $remember = isset($_POST['remember']);

    // Валидация
    if (empty($email) || empty($password)) {
        die('Все поля обязательны для заполнения.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Некорректный email.');
    }

    // Здесь должна быть проверка в базе данных
    // Пример условного логина:
    if ($email === 'user@example.com' && $password === 'secret123') {
        $_SESSION['user_email'] = $email;
        if ($remember) {
            setcookie('user_email', $email, time() + 30 * 24 * 3600, '/');
        }
        header('Location: dashboard.php');
        exit;
    } else {
        echo 'Неверные учетные данные.';
    }
}
?>
