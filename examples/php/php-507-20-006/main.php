<?php
$result = $mysqli->query("SELECT * FROM users ORDER BY id DESC");

// Вариант 1: через цикл
while ($user = $result->fetch_assoc()) {
    echo $user['name'] . " - " . $user['email'] . "<br>";
}

// Вариант 2: все сразу в массив
$users = $result->fetch_all(MYSQLI_ASSOC);
foreach ($users as $user) {
    echo $user['name'] . "<br>";
}

// Вариант 3: как объекты
while ($user = $result->fetch_object()) {
    echo $user->name . "<br>";
}
?>
