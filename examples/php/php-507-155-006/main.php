<?php
session_start();
require_once '../includes/db.php';

$errors = [];

if ($_POST) {
    $username = trim($_POST['username'] ?? '');
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'] ?? '';

    // Валидация
    if (strlen($username) < 3) {
        $errors[] = "Логин должен быть не короче 3 символов";
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Некорректный email";
    }
    if (strlen($password) < 8) {
        $errors[] = "Пароль должен содержать минимум 8 символов";
    }

    // Проверка уникальности логина и email
    if (empty($errors)) {
        $stmt = $pdo->prepare("SELECT id FROM users WHERE username = ? OR email = ?");
        $stmt->execute([$username, $email]);
        if ($stmt->fetch()) {
            $errors[] = "Пользователь с таким логином или email уже существует";
        }
    }

    if (empty($errors)) {
        $hash = password_hash($password, PASSWORD_ARGON2ID);
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, 'user')");
        $stmt->execute([$username, $email, $hash]);

        // Автоматический вход после регистрации (опционально)
        $_SESSION['user_id'] = $pdo->lastInsertId();
        $_SESSION['username'] = $username;
        $_SESSION['role'] = 'user';
        $_SESSION['logged_in'] = true;
        session_regenerate_id(true);

        header("Location: /dashboard.php");
        exit;
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Регистрация</title>
</head>
<body>
    <h1>Регистрация</h1>

    <?php if (!empty($errors)): ?>
        <div style="color: red;">
            <?php foreach ($errors as $error): ?>
                <p><?= htmlspecialchars($error) ?></p>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>

    <form method="post">
        <label>
            Логин:<br>
            <input type="text" name="username" required>
        </label><br><br>

        <label>
            Email:<br>
            <input type="email" name="email" required>
        </label><br><br>

        <label>
            Пароль:<br>
            <input type="password" name="password" required>
        </label><br><br>

        <button type="submit">Зарегистрироваться</button>
    </form>

    <p><a href="/auth/login.php">Уже есть аккаунт? Войти</a></p>
</body>
</html>
