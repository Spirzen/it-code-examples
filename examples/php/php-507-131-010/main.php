<?php
/**
 * Мониторинг дискового пространства
 */

$diskInfo = disk_free_space('/');
$totalSpace = disk_total_space('/');
$usedSpace = $totalSpace - $diskInfo;
$percentUsed = round(($usedSpace / $totalSpace) * 100, 2);

echo "Диск: /\n";
echo "Всего места: " . formatBytes($totalSpace) . "\n";
echo "Занято: " . formatBytes($usedSpace) . " ({$percentUsed}%)\n";
echo "Свободно: " . formatBytes($diskInfo) . "\n";

function formatBytes(int $bytes, int $precision = 2): string {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $bytes = max($bytes, 0);
    $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
    $pow = min($pow, count($units) - 1);
    $bytes /= pow(1024, $pow);
    return round($bytes, $precision) . ' ' . $units[$pow];
}
?>
