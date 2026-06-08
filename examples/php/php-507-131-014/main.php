<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Динамическая форма</title>
</head>
<body>
    <h1>Обратная связь</h1>

    <?php
    $message = '';
    $errors = [];

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $name = trim($_POST['name'] ?? '');
        $email = trim($_POST['email'] ?? '');
        $comment = trim($_POST['comment'] ?? '');

        if (empty($name)) {
            $errors[] = 'Имя обязательно.';
        }

        if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors[] = 'Введите корректный email.';
        }

        if (empty($comment)) {
            $errors[] = 'Комментарий обязателен.';
        }

        if (empty($errors)) {
            $message = "Спасибо, {$name}! Ваша заявка принята.";
            // Здесь могла бы быть логика сохранения в базу данных
        }
    }
    ?>

    <?php if (!empty($errors)): ?>
        <div style="color: red;">
            <ul>
                <?php foreach ($errors as $error): ?>
                    <li><?php echo htmlspecialchars($error); ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>

    <?php if ($message): ?>
        <div style="color: green;">
            <p><?php echo htmlspecialchars($message); ?></p>
        </div>
    <?php endif; ?>

    <form method="POST" action="">
        <label>Имя:<br><input type="text" name="name"></label><br><br>
        <label>Email:<br><input type="email" name="email"></label><br><br>
        <label>Комментарий:<br><textarea name="comment"></textarea></label><br><br>
        <button type="submit">Отправить</button>
    </form>
</body>
</html>
