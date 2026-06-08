<?php
$host = '127.0.0.1';
$user = 'root';
$pass = '';
$db   = 'mysql';

$link = mysqli_connect($host, $user, $pass, $db);
if (!$link) {
    die('Ошибка: ' . mysqli_connect_error());
}

$result = mysqli_query($link, 'SHOW DATABASES');
while ($row = mysqli_fetch_assoc($result)) {
    echo $row['Database'] . "\n";
}
mysqli_close($link);
