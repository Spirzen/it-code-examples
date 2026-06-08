<?php
if ($_POST) {
    $username = trim($_POST['username']);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'];

    // Валидация
    if (strlen($password) < 8) {
        die("Пароль должен быть не менее 8 символов");
    }

    // Хеширование
    $hash = password_hash($password, PASSWORD_ARGON2ID);

    // Сохранение в БД (пример с PDO)
    $stmt = $pdo->prepare("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)");
    $stmt->execute([$username, $email, $hash]);

    // Перенаправление на страницу входа
    header("Location: login.php");
    exit;
}
?>
<form method="post">
    <input name="username" placeholder="Логин" required>
    <input name="email" type="email" placeholder="Email" required>
    <input name="password" type="password" placeholder="Пароль" required>
    <button>Зарегистрироваться</button>
</form>
