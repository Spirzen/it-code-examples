<?php
require_once 'config.php';

if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
    exit;
}

$stmt = $pdo->prepare("SELECT email, created_at FROM users WHERE id = ?");
$stmt->execute([$_SESSION['user_id']]);
$user = $stmt->fetch();
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Личный кабинет</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        .user-info { background: #f8f9fa; padding: 20px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Личный кабинет</h1>
    
    <div class="user-info">
        <p><strong>Email:</strong> <?php echo htmlspecialchars($user['email']); ?></p>
        <p><strong>Дата регистрации:</strong> <?php echo htmlspecialchars($user['created_at']); ?></p>
    </div>
    
    <form action="logout.php" method="post">
        <button type="submit" style="background: #dc3545; color: white; border: none; padding: 10px 20px; cursor: pointer;">
            Выйти из системы
        </button>
    </form>
</body>
</html>
