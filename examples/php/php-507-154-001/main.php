if (($_FILES['avatar']['error'] ?? UPLOAD_ERR_NO_FILE) === UPLOAD_ERR_OK) {
    $tmpName = $_FILES['avatar']['tmp_name'];
    if (!is_uploaded_file($tmpName)) {
        exit('Недопустимый источник файла');
    }
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mime = $finfo->file($tmpName);
    $allowed = ['image/jpeg' => 'jpg', 'image/png' => 'png'];
    if (!isset($allowed[$mime])) {
        exit('Разрешены только JPEG и PNG');
    }
    $target = __DIR__ . '/uploads/' . bin2hex(random_bytes(16)) . '.' . $allowed[$mime];
    if (move_uploaded_file($tmpName, $target)) {
        echo 'Файл загружен.';
    }
}
