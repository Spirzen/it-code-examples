<?php
declare(strict_types=1);

function createUser(array $payload): array
{
    $email = trim((string)($payload["email"] ?? ""));
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Некорректный email");
    }

    return [
        "email" => $email,
        "age" => (int)($payload["age"] ?? 0),
        "active" => (bool)($payload["active"] ?? false),
    ];
}
