<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'] ?? '';
    $confirm = $_POST['confirm'] ?? '';

    // Валидация
    if (empty($name) || empty($email) || empty($password) || empty($confirm)) {
        die('Все поля обязательны.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Некорректный email.');
    }

    if ($password !== $confirm) {
        die('Пароли не совпадают.');
    }

    if (strlen($password) < 8) {
        die('Пароль должен содержать минимум 8 символов.');
    }

    // Проверка сложности пароля (пример)
    if (!preg_match('/[A-Z]/', $password) || !preg_match('/[0-9]/', $password)) {
        die('Пароль должен содержать хотя бы одну заглавную букву и одну цифру.');
    }

    // Проверка уникальности email (в реальном проекте — запрос к БД)
    // if (emailExists($email)) { die('Пользователь с таким email уже существует.'); }

    // Хеширование пароля
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Сохранение в БД
    // insertUser($name, $email, $hashedPassword);

    echo 'Регистрация успешна! <a href="login.php">Войдите</a>.';
}
?>
