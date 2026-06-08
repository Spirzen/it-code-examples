<?php
$user_id = 5;

$stmt = $mysqli->prepare("DELETE FROM users WHERE id = ?");
$stmt->bind_param("i", $user_id);

if ($stmt->execute()) {
    echo "Удалено строк: " . $stmt->affected_rows;
} else {
    echo "Ошибка: " . $stmt->error;
}

$stmt->close();
?>
