<?php
/**
 * Создание резервной копии
 * Использование: php backup.php <путь_к_папке> <путь_для_резерва>
 */

$sourceDir = $argv[1] ?? '.';
$backupDir = $argv[2] ?? './backups';
$date = date('Y-m-d_H-i-s');
$backupName = "backup_{$date}.zip";
$backupPath = $backupDir . '/' . $backupName;

if (!is_dir($sourceDir)) {
    die("Ошибка: Исходная директория не найдена\n");
}

if (!is_dir($backupDir)) {
    mkdir($backupDir, 0755, true);
}

$zip = new ZipArchive();

if ($zip->open($backupPath, ZipArchive::CREATE | ZipArchive::OVERWRITE) !== TRUE) {
    die("Ошибка: Не удалось создать архив\n");
}

$iterator = new RecursiveIteratorIterator(
    new RecursiveDirectoryIterator($sourceDir, RecursiveDirectoryIterator::SKIP_DOTS),
    RecursiveIteratorIterator::SELF_FIRST
);

foreach ($iterator as $file) {
    $filePath = $file->getPathname();
    $relativePath = $file->getRelativePathname();

    if ($file->isDir()) {
        $zip->addEmptyDir($relativePath);
    } else {
        $zip->addFile($filePath, $relativePath);
    }
}

$zip->close();
echo "Резервная копия создана: {$backupPath}\n";
echo "Размер архива: " . filesize($backupPath) . " байт\n";
?>
