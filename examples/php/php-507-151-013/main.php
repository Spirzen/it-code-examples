<?php
declare(strict_types=1);

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    exit;
}

$input = [
    "email" => trim((string)($_POST["email"] ?? "")),
    "message" => trim((string)($_POST["message"] ?? "")),
];

$errors = [];
if (!filter_var($input["email"], FILTER_VALIDATE_EMAIL)) {
    $errors["email"] = "Некорректный email";
}
if ($input["message"] === "") {
    $errors["message"] = "Сообщение обязательно";
}

if ($errors !== []) {
    http_response_code(422);
    // Вернуть ошибки в шаблон или JSON
    exit;
}

// saveMessage($input);
header("Location: /thank-you.php");
exit;
