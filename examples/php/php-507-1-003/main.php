<?php
$pdo = new PDO('mysql:host=localhost;dbname=shop', 'user', 'password');

// Статический запрос без пользовательского ввода — допустим query()
$stmt = $pdo->query('SELECT id, name, price FROM products ORDER BY id');
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    echo '<div>' . htmlspecialchars($row['name'], ENT_QUOTES, 'UTF-8')
        . ' — ' . htmlspecialchars((string) $row['price'], ENT_QUOTES, 'UTF-8') . ' руб.</div>';
}

// Любые данные от пользователя — только prepared statement
$email = $_GET['email'] ?? '';
$stmt = $pdo->prepare('SELECT id, name FROM users WHERE email = ?');
$stmt->execute([$email]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);
?>
