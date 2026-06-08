<?php
session_start();
$role = $_SESSION['role'] ?? 'guest';
?>

<nav>
    <a href="/">Главная</a>
    <?php if ($role === 'user' || $role === 'admin'): ?>
        <a href="/profile">Профиль</a>
    <?php endif; ?>
    <?php if ($role === 'admin'): ?>
        <a href="/admin">Админка</a>
    <?php endif; ?>
</nav>
