<?php
session_start();
require_once 'includes/auth.php';
requireLogin(); // Требует входа

$title = "Панель управления";
$role = getUserRole();
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title><?= htmlspecialchars($title) ?></title>
</head>
<body>
    <h1>Добро пожаловать, <?= htmlspecialchars($_SESSION['username']) ?>!</h1>
    <p>Ваша роль: <strong><?= htmlspecialchars($role) ?></strong></p>

    <nav>
        <a href="/">Главная</a> |
        <a href="/auth/logout.php">Выйти</a>
    </nav>

    <?php if (hasRole('admin')): ?>
        <div style="margin-top: 20px; padding: 10px; background: #e0f7fa;">
            <h2>Административная зона</h2>
            <ul>
                <li><a href="/admin/users.php">Управление пользователями</a></li>
                <li><a href="/admin/logs.php">Логи системы</a></li>
            </ul>
        </div>
    <?php endif; ?>

    <?php if (hasRole('user')): ?>
        <div style="margin-top: 20px;">
            <h2>Ваши данные</h2>
            <p>Вы можете редактировать профиль, менять пароль и просматривать историю действий.</p>
        </div>
    <?php endif; ?>
</body>
</html>
