<?php
$user_id = 1;

$stmt = $mysqli->prepare("SELECT * FROM users WHERE id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();

if ($row = $result->fetch_assoc()) {
    echo "Имя: " . $row['name'] . "<br>";
    echo "Email: " . $row['email'] . "<br>";
    echo "Возраст: " . $row['age'];
}

$stmt->close();
?>
