try {
    $stmt = $pdo->prepare(
        'INSERT INTO subscribers (name, email, created_at) VALUES (:name, :email, :created_at)'
    );
    $stmt->execute([
        'name'       => $name,
        'email'      => $email,
        'created_at' => (new DateTimeImmutable('now'))->format('Y-m-d H:i:s'),
    ]);
} catch (PDOException $e) {
    // Дубликат email (код 23000 — integrity constraint)
    if ((int) ($e->errorInfo[1] ?? 0) === 1062) {
        header('Location: register.php?error=duplicate');
        exit;
    }
    error_log($e->getMessage());
    http_response_code(500);
    echo 'Ошибка сервера';
    exit;
}

header('Location: thanks.php', true, 302);
exit;
