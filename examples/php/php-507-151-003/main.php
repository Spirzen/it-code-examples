if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['document']) && $_FILES['document']['error'] === UPLOAD_ERR_OK) {
        $tmpPath = $_FILES['document']['tmp_name'];
        $targetDir = __DIR__ . '/uploads/';

        if (!is_uploaded_file($tmpPath)) {
            die('Недопустимая загрузка');
        }

        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mime = $finfo->file($tmpPath);
        $allowedMimes = ['image/jpeg', 'image/png', 'application/pdf'];
        if (!in_array($mime, $allowedMimes, true)) {
            die('Недопустимый тип файла');
        }

        $storedName = bin2hex(random_bytes(16)) . match ($mime) {
            'image/jpeg' => '.jpg',
            'image/png' => '.png',
            'application/pdf' => '.pdf',
            default => '',
        };
        $targetPath = $targetDir . $storedName;

        if (move_uploaded_file($tmpPath, $targetPath)) {
            echo "Файл успешно загружен";
        } else {
            echo "Ошибка при сохранении файла";
        }
    } else {
        echo "Ошибка загрузки: " . $_FILES['document']['error'];
    }
}
