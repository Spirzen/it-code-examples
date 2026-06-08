<?php
// HTML форма с method="POST"
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    
    // Валидация
    $name = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
    $email = filter_var($email, FILTER_VALIDATE_EMAIL);
    
    if ($email) {
        echo "Привет, $name! Твой email: $email";
    } else {
        echo "Неверный email";
    }
}
?>
