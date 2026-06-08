// Добавление
$colors[] = 'yellow'; // в конец
$user['email'] = 'bob@example.com';

// Чтение
echo $user['name']; // Bob

// Итерация
foreach ($user as $key => $value) {
    echo "$key: $value\n";
}

// Проверка существования ключа
if (isset($user['email'])) { /* ... */ }
