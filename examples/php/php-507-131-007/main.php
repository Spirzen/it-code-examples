<?php
/**
 * Отправитель HTTP-запросов
 * Использование: php send_request.php <url> <json_data>
 */

$url = $argv[1] ?? '';
$jsonData = $argv[2] ?? '{}';

if (empty($url)) {
    die("Укажите URL адрес\n");
}

$ch = curl_init();

curl_setopt_array($ch, [
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $jsonData,
    CURLOPT_HTTPHEADER => [
        'Content-Type: application/json',
        'Content-Length: ' . strlen($jsonData)
    ]
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$error = curl_error($ch);

curl_close($ch);

if ($error) {
    echo "Ошибка: {$error}\n";
} else {
    echo "Статус: {$httpCode}\n";
    echo "Ответ: {$response}\n";
}
?>
