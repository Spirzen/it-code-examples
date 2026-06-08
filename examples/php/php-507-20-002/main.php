// Привязать параметры (заменить ? на реальные значения)
$stmt->bind_param("sss", $username, $email, $password_hash);

// Выполнить запрос
$stmt->execute();

// Получить результат (для SELECT)
$result = $stmt->get_result();

// Узнать количество затронутых строк
$stmt->affected_rows;

// Закрыть запрос
$stmt->close();
