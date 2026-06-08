<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Некорректный email.');
    }

    // Проверка существования пользователя (в реальности — запрос к БД)
    // if (!userExists($email)) { ... }

    // Генерация токена (пример)
    $token = bin2hex(random_bytes(32));
    // Сохранение токена в БД с временем жизни (например, 1 час)

    // Отправка письма (в реальности — через PHPMailer и т.п.)
    // $link = "https://example.com/set_new_password.php?token=$token";
    // mail($email, "Сброс пароля", "Перейдите по ссылке: $link");

    echo '<p style="color: green; text-align: center;">Ссылка для сброса пароля отправлена на ваш email.</p>';
}
?>
