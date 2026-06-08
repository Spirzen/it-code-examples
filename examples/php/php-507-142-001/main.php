<?php

$raw = file_get_contents("php://input");
$payload = json_decode($raw, true);

if (!is_array($payload) || empty($payload["email"])) {
    http_response_code(422);
    echo json_encode(["error" => "email is required"]);
    exit;
}

$email = trim((string) $payload["email"]);
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(["error" => "invalid email"]);
    exit;
}

echo json_encode(["ok" => true, "email" => $email]);
