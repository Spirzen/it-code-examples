<?php
// Подключение к базе данных SQLite
$db = new SQLite3('mydb.sq3');

// SQL-запрос: выборка товаров дешевле 3.00
$sql = "SELECT * FROM items WHERE price < 3.00";
$result = $db->query($sql);

// Вывод результатов
while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
    echo $row['name'] . ': $' . $row['price'] . '<br/>';
}

// Освобождение ресурсов
unset($db);
?>
