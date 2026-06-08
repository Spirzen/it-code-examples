<?php
/**
 * Простой HTTP-клиент
 * Использование: php client.php <host> <port>
 */

$host = $argv[1] ?? '127.0.0.1';
$port = $argv[2] ?? 8080;

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

if (!socket_connect($socket, $host, $port)) {
    die("Ошибка подключения к серверу\n");
}

$request = "GET / HTTP/1.1\r\nHost: {$host}:{$port}\r\n\r\n";
socket_write($socket, $request, strlen($request));

$response = socket_read($socket, 2048);
echo "Ответ от сервера:\n{$response}\n";

socket_close($socket);
?>
