<?php
declare(strict_types=1);

function loadConfig(string $path): array
{
    if (!is_readable($path)) {
        throw new \RuntimeException("Config not readable: {$path}");
    }

    $json = file_get_contents($path);
    $data = json_decode($json, true, flags: JSON_THROW_ON_ERROR);
    return $data;
}

try {
    $config = loadConfig(__DIR__ . '/config.json');
} catch (\JsonException $e) {
    fwrite(STDERR, "Invalid JSON: " . $e->getMessage() . PHP_EOL);
    $config = [];
} catch (\RuntimeException $e) {
    fwrite(STDERR, $e->getMessage() . PHP_EOL);
    $config = [];
} finally {
    // Выполняется всегда: и после успеха, и после catch, и перед exit в catch
    // Закрытие ресурсов, сброс флагов — сюда
}
