<?php
/**
 * Минимальный HTTP-сервер на PHP
 * Запуск: php server.php 8080
 */

$host = '127.0.0.1';
$port = $argv[1] ?? 8080;

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($socket, $host, $port);
socket_listen($socket);

echo "Сервер запущен на http://{$host}:{$port}\n";

while (true) {
    $client = socket_accept($socket);
    
    if ($client === false) {
        continue;
    }

    $request = socket_read($client, 2048);
    $response = "HTTP/1.1 200 OK\r\n";
    $response .= "Content-Type: text/plain\r\n";
    $response .= "\r\n";
    $response .= "Hello from PHP Server! Request received.";

    socket_write($client, $response, strlen($response));
    socket_close($client);
}

socket_close($socket);
?>
