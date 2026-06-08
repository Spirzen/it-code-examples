<?php

declare(strict_types=1);

function detectMime(string $path): string
{
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    return $finfo->file($path) ?: 'application/octet-stream';
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit('Method Not Allowed');
}

$file = $_FILES['document'] ?? null;

if ($file === null || $file['error'] !== UPLOAD_ERR_OK) {
    http_response_code(400);
    exit('Ошибка загрузки');
}

$tmp = $file['tmp_name'];
$maxBytes = 5 * 1024 * 1024;
$allowedMimes = ['application/pdf' => 'pdf'];

if ($file['size'] > $maxBytes || !is_uploaded_file($tmp)) {
    http_response_code(400);
    exit('Файл отклонён');
}

$mime = detectMime($tmp);
if (!isset($allowedMimes[$mime])) {
    http_response_code(400);
    exit('Допустим только PDF');
}

$extension = $allowedMimes[$mime];
$storedName = bin2hex(random_bytes(16)) . '.' . $extension;
$uploadDir = __DIR__ . '/../var/uploads';
$target = $uploadDir . '/' . $storedName;

if (!is_dir($uploadDir) && !mkdir($uploadDir, 0750, true)) {
    http_response_code(500);
    exit('Каталог недоступен');
}

if (!move_uploaded_file($tmp, $target)) {
    http_response_code(500);
    exit('Не удалось сохранить файл');
}

// $file['name'] — только для UI или записи в БД как "оригинальное имя"
