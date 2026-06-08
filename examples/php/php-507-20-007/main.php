<?php
$user_id = 1;
$new_email = "newemail@example.com";
$new_age = 26;

$stmt = $mysqli->prepare("UPDATE users SET email = ?, age = ? WHERE id = ?");
$stmt->bind_param("sii", $new_email, $new_age, $user_id);

if ($stmt->execute()) {
    $affected = $stmt->affected_rows;
    echo "Обновлено строк: " . $affected;
} else {
    echo "Ошибка: " . $stmt->error;
}

$stmt->close();
?>
