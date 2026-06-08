<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!isset($_FILES['uploaded_file'])) {
        die('Файл не был отправлен.');
    }

    $file = $_FILES['uploaded_file'];
    $uploadDir = __DIR__ . '/uploads/';
    $maxSize = 5 * 1024 * 1024; // 5 МБ
    $allowedTypes = ['image/jpeg', 'image/png', 'application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];

    // Проверка ошибок
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die('Ошибка при загрузке файла.');
    }

    // Проверка размера
    if ($file['size'] > $maxSize) {
        die('Файл слишком большой (макс. 5 МБ).');
    }

    // Проверка типа
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mimeType = finfo_file($finfo, $file['tmp_name']);
    finfo_close($finfo);

    if (!in_array($mimeType, $allowedTypes)) {
        die('Недопустимый тип файла.');
    }

    // Генерация безопасного имени
    $extension = pathinfo($file['name'], PATHINFO_EXTENSION);
    $safeName = bin2hex(random_bytes(16)) . '.' . strtolower($extension);
    $targetPath = $uploadDir . $safeName;

    // Создание директории, если её нет
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0755, true);
    }

    // Перемещение файла
    if (move_uploaded_file($file['tmp_name'], $targetPath)) {
        echo "Файл успешно загружен! <br>Путь: " . htmlspecialchars($targetPath);
    } else {
        die('Не удалось сохранить файл.');
    }
}
?>
