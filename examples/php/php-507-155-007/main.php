<?php
session_start();
require_once '../includes/db.php';

$errors = [];

if ($_POST) {
    $identifier = trim($_POST['identifier'] ?? ''); // может быть логин или email
    $password = $_POST['password'] ?? '';

    if (empty($identifier) || empty($password)) {
        $errors[] = "Заполните все поля";
    } else {
        // Поиск по логину или email
        $stmt = $pdo->prepare("SELECT id, username, email, password_hash, role FROM users WHERE username = ? OR email = ?");
        $stmt->execute([$identifier, $identifier]);
        $user = $stmt->fetch();

        if ($user && password_verify($password, $user['password_hash'])) {
            // Успешная аутентификация
            session_regenerate_id(true);
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            $_SESSION['role'] = $user['role'];
            $_SESSION['logged_in'] = true;

            // Перенаправление на предыдущую страницу или на дашборд
            $redirect = $_GET['redirect'] ?? '/dashboard.php';
            header("Location: " . $redirect);
            exit;
        } else {
            $errors[] = "Неверный логин/email или пароль";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вход</title>
</head>
<body>
    <h1>Вход в систему</h1>

    <?php if (!empty($errors)): ?>
        <div style="color: red;">
            <?php foreach ($errors as $error): ?>
                <p><?= htmlspecialchars($error) ?></p>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>

    <form method="post">
        <label>
            Логин или email:<br>
            <input type="text" name="identifier" required>
        </label><br><br>

        <label>
            Пароль:<br>
            <input type="password" name="password" required>
        </label><br><br>

        <button type="submit">Войти</button>
    </form>

    <p><a href="/auth/register.php">Нет аккаунта? Зарегистрироваться</a></p>
</body>
</html>
