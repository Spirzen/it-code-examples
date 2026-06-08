<?php
/**
 * Сканирование директории
 * Использование: php scan_dir.php <путь>
 */

$path = $argv[1] ?? '.';

if (!is_dir($path)) {
    die("Ошибка: Путь не существует или не является директорией\n");
}

$iterator = new RecursiveIteratorIterator(
    new RecursiveDirectoryIterator($path, RecursiveDirectoryIterator::SKIP_DOTS),
    RecursiveIteratorIterator::SELF_FIRST
);

echo "Сканирование директории: {$path}\n";
echo str_repeat('-', 40) . "\n";

foreach ($iterator as $file) {
    $relativePath = $file->getRelativePathname();
    $size = $file->getSize();
    $type = $file->isDir() ? '[DIR]' : '[FILE]';
    $permissions = substr(sprintf('%o', $file->getPerms()), -4);

    echo "{$type} {$relativePath} | Размер: {$size} байт | Права: {$permissions}\n";
}
?>
