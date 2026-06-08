<?php
session_start();

$errors = [];
$formData = [];
$message = null;

if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'] ?? '')) {
        $errors['form'] = 'Недействительный запрос. Обновите страницу.';
    } else {
        $formData['name'] = trim($_POST['name'] ?? '');
        $formData['age'] = $_POST['age'] ?? '';
        $formData['email'] = trim($_POST['email'] ?? '');
        $formData['message'] = trim($_POST['message'] ?? '');

        if ($formData['name'] === '') {
            $errors['name'] = 'Имя обязательно';
        } elseif (strlen($formData['name']) < 2) {
            $errors['name'] = 'Имя должно содержать минимум 2 символа';
        }

        if (!filter_var($formData['email'], FILTER_VALIDATE_EMAIL)) {
            $errors['email'] = 'Введите корректный email';
        }

        $age = filter_var($formData['age'], FILTER_VALIDATE_INT);
        if ($age === false || $age < 0 || $age > 120) {
            $errors['age'] = 'Введите корректный возраст (0–120)';
        }

        if ($errors === []) {
            $message = "Привет, {$formData['name']}! Тебе {$age} лет.";
            // Сохранение в БД — только через prepare(), см. пример PDO ниже
        }
    }
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Форма ввода</title>
</head>
<body>
    <?php if ($message !== null): ?>
        <div style="color: green;"><?= htmlspecialchars($message, ENT_QUOTES, 'UTF-8') ?></div>
    <?php endif; ?>
    <?php if (isset($errors['form'])): ?>
        <div style="color: red;"><?= htmlspecialchars($errors['form'], ENT_QUOTES, 'UTF-8') ?></div>
    <?php endif; ?>

    <form method="post">
        <input type="hidden" name="csrf_token" value="<?= htmlspecialchars($_SESSION['csrf_token'], ENT_QUOTES, 'UTF-8') ?>">
        <div>
            <label>Имя:</label>
            <input type="text" name="name" value="<?= htmlspecialchars($formData['name'] ?? '', ENT_QUOTES, 'UTF-8') ?>">
            <?php if (isset($errors['name'])): ?>
                <span style="color: red;"><?= htmlspecialchars($errors['name'], ENT_QUOTES, 'UTF-8') ?></span>
            <?php endif; ?>
        </div>
        <div>
            <label>Возраст:</label>
            <input type="number" name="age" value="<?= htmlspecialchars((string) ($formData['age'] ?? ''), ENT_QUOTES, 'UTF-8') ?>">
            <?php if (isset($errors['age'])): ?>
                <span style="color: red;"><?= htmlspecialchars($errors['age'], ENT_QUOTES, 'UTF-8') ?></span>
            <?php endif; ?>
        </div>
        <div>
            <label>Email:</label>
            <input type="email" name="email" value="<?= htmlspecialchars($formData['email'] ?? '', ENT_QUOTES, 'UTF-8') ?>">
            <?php if (isset($errors['email'])): ?>
                <span style="color: red;"><?= htmlspecialchars($errors['email'], ENT_QUOTES, 'UTF-8') ?></span>
            <?php endif; ?>
        </div>
        <div>
            <label>Сообщение:</label>
            <textarea name="message"><?= htmlspecialchars($formData['message'] ?? '', ENT_QUOTES, 'UTF-8') ?></textarea>
        </div>
        <button type="submit">Отправить</button>
    </form>
</body>
</html>
