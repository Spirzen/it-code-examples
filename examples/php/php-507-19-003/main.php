<?php
try {
    // Подключение с режимом исключения
    $pdo = new PDO(
        'mysql:host=localhost;dbname=test;charset=utf8mb4',
        'user',
        'password',
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
    );

    // Начало транзации
    $pdo->beginTransaction();

    // Подготовка первого запроса
    $stmt1 = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
    $stmt1->execute([
        ':name' => 'Иван Иванов',
        ':email' => 'ivan@example.com'
    ]);

    // Имитация второго действия (например, обновление баланса)
    $stmt2 = $pdo->prepare("UPDATE accounts SET balance = balance - 100 WHERE user_id = 1");
    $stmt2->execute();

    // Если код дошел сюда — все успешно
    $pdo->commit();
    echo "Транзакция успешно завершена.";

} catch (PDOException $e) {
    // При любой ошибке база данных автоматически откатит изменения
    if ($pdo->inTransaction()) {
        $pdo->rollBack();
    }
    // Логирование ошибки или вывод пользователю
    error_log("Ошибка базы данных: " . $e->getMessage());
    throw new Exception("Не удалось выполнить операцию", 0, $e);

} finally {
    // Этот блок выполнится всегда, даже если выбросили исключение выше
    // Здесь можно закрыть соединения или сбросить флаги
    echo "\nБлок finally выполнен.";
}
