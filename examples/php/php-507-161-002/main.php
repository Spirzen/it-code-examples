<?php
declare(strict_types=1);

require dirname(__DIR__) . '/bootstrap.php';

$name  = trim((string) ($_POST['name'] ?? ''));
$email = trim((string) ($_POST['email'] ?? ''));

$errors = [];

if ($name === '') {
    $errors['name'] = 'Укажите имя';
} elseif (mb_strlen($name) > 100) {
    $errors['name'] = 'Имя слишком длинное';
}

if ($email === '') {
    $errors['email'] = 'Укажите email';
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors['email'] = 'Некорректный email';
}

if ($errors !== []) {
    // Упрощение: редирект с флагом; в реальном проекте — сессия с полями и ошибками
    header('Location: register.php?error=1');
    exit;
}
