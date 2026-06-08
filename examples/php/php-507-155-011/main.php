<?php
require_once '../includes/db.php';

$token = $_GET['token'] ?? '';
if (!$token) {
    die("Недействительная ссылка");
}

// Поиск токена
$stmt = $pdo->prepare("
    SELECT pr.user_id, pr.expires_at, u.email 
    FROM password_resets pr 
    JOIN users u ON pr.user_id = u.id 
    WHERE pr.token = ?
");
$stmt->execute([$token]);
$record = $stmt->fetch();

if (!$record) {
    die("Ссылка недействительна или устарела");
}

$expires = strtotime($record['expires_at']);
if (time() > $expires) {
    die("Срок действия ссылки истёк");
}

if ($_POST) {
    $password = $_POST['password'] ?? '';
    if (strlen($password) < 8) {
        $error = "Пароль должен быть не короче 8 символов";
    } else {
        $hash = password_hash($password, PASSWORD_ARGON2ID);
        $pdo->prepare("UPDATE users SET password_hash = ? WHERE id = ?")
            ->execute([$hash, $record['user_id']]);

        // Удаление использованного токена
        $pdo->prepare("DELETE FROM password_resets WHERE token = ?")->execute([$token]);

        echo "<p>Пароль успешно изменён. <a href='/auth/login.php'>Войти</a></p>";
        exit;
    }
}
?>

<form method="post">
    <h2>Новый пароль</h2>
    <?php if (!empty($error)): ?>
        <p style="color:red"><?= htmlspecialchars($error) ?></p>
    <?php endif; ?>
    <label>Пароль:<br><input type="password" name="password" required></label><br><br>
    <button>Сохранить</button>
</form>
