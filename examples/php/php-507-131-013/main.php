<?php
/**
 * Просмотр запущенных процессов
 * Работает только в Linux/Unix системах
 */

if (PHP_OS_FAMILY !== 'Linux' && PHP_OS_FAMILY !== 'BSD') {
    die("Эта утилита работает только в Linux или BSD системах\n");
}

$processes = shell_exec('ps aux');
$lines = explode("\n", trim($processes));

echo "ID\t\tUSER\t\tCPU%\tMEM%\tCOMMAND\n";
echo str_repeat('-', 80) . "\n";

array_shift($lines); // Удаление заголовка ps

foreach ($lines as $line) {
    $parts = preg_split('/\s+/', trim($line));
    
    if (count($parts) >= 11) {
        $pid = $parts[1];
        $user = $parts[2];
        $cpu = $parts[2]; // Индекс может варьироваться в зависимости от системы, здесь упрощено
        $mem = $parts[3];
        $cmd = $parts[10] ?? '';
        
        // Корректировка индексов для стандартного ps aux
        $pid = $parts[1];
        $user = $parts[2];
        $cpu = $parts[2]; // Это поле CPU%
        $mem = $parts[3]; // Это поле MEM%
        $cmd = implode(' ', array_slice($parts, 10));
        
        echo "{$pid}\t\t{$user}\t\t{$cpu}\t\t{$mem}\t\t{$cmd}\n";
    }
}
?>
