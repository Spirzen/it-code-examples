<?php
/**
 * Парсер URL и проверка доступности
 * Использование: php check_url.php <url>
 */

$url = $argv[1] ?? '';

if (empty($url)) {
    die("Укажите URL\n");
}

$parsedUrl = parse_url($url);

echo "Парсинг URL: {$url}\n";
echo "Протокол: " . ($parsedUrl['scheme'] ?? 'нет') . "\n";
echo "Хост: " . ($parsedUrl['host'] ?? 'нет') . "\n";
echo "Порт: " . ($parsedUrl['port'] ?? 'нет') . "\n";
echo "Путь: " . ($parsedUrl['path'] ?? '/') . "\n";
echo "Запрос: " . ($parsedUrl['query'] ?? '') . "\n";

// Проверка доступности
$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_NOBODY => true, // Только заголовки
    CURLOPT_TIMEOUT => 5
]);

curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Статус доступности: " . getStatusMessage($httpCode) . "\n";

function getStatusMessage(int $code): string {
    switch ($code) {
        case 200: return "OK";
        case 404: return "Не найдено";
        case 500: return "Ошибка сервера";
        default: return "Статус {$code}";
    }
}
?>
