<?php
session_start();
require_once '../includes/db.php';

if ($_POST) {
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Некорректный email";
    } else {
        // Поиск пользователя
        $stmt = $pdo->prepare("SELECT id, email FROM users WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch();

        if ($user) {
            // Генерация токена
            $token = bin2hex(random_bytes(32));
            $expires = time() + 1800; // 30 минут

            // Сохранение в БД
            $stmt = $pdo->prepare("INSERT INTO password_resets (user_id, token, expires_at) VALUES (?, ?, ?)");
            $stmt->execute([$user['id'], $token, date('Y-m-d H:i:s', $expires)]);

            // Отправка email (здесь — заглушка)
            $resetLink = "https://example.com/auth/reset.php?token=" . urlencode($token);
            // mail($email, "Восстановление пароля", "Перейдите по ссылке: $resetLink");

            // В реальном проекте используйте PHPMailer или аналог
            echo "<p>Ссылка для восстановления отправлена на ваш email.</p>";
            exit;
        }

        // Всегда показываем одинаковое сообщение
        echo "<p>Если указанный email зарегистрирован, вы получите инструкции.</p>";
        exit;
    }
}
?>

<form method="post">
    <label>Email:<br><input type="email" name="email" required></label><br><br>
    <button>Восстановить пароль</button>
</form>
