<?php
$mysqli = new mysqli("localhost", "user", "password", "database_name");

// Отключение режима автокоммита
$mysqli->autocommit(false);

try {
    // Начало транзакции
    $mysqli->begin_transaction();

    // Первый запрос
    $stmt1 = $mysqli->prepare("UPDATE accounts SET balance = balance - ? WHERE id = ?");
    $amount = 100;
    $from_id = 1;
    $stmt1->bind_param("di", $amount, $from_id);
    $stmt1->execute();
    $stmt1->close();

    // Второй запрос
    $stmt2 = $mysqli->prepare("UPDATE accounts SET balance = balance + ? WHERE id = ?");
    $to_id = 2;
    $stmt2->bind_param("di", $amount, $to_id);
    $stmt2->execute();
    $stmt2->close();

    // Установка точки сохранения
    $mysqli->savepoint("step_2");

    // Симуляция успешного завершения
    // Если бы произошла ошибка, можно было бы вызвать rollback() или rollback to savepoint
    
    // Подтверждение транзакции
    $mysqli->commit();
    echo "Транзакция успешно завершена.\n";

} catch (Exception $e) {
    // Откат транзакции при ошибке
    $mysqli->rollback();
    echo "Транзакция отменена: {$e->getMessage()}\n";
} finally {
    // Возврат режима автокоммита в исходное состояние
    $mysqli->autocommit(true);
    $mysqli->close();
}
?>
