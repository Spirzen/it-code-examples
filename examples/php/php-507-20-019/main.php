<?php
// Имитация получения данных из $_FILES (для примера используем переменную)
// В реальном коде используйте: $_FILES['uploaded_file']['tmp_name']
$tmpFileName = $_FILES['uploaded_file']['tmp_name'] ?? null;

if ($tmpFileName && is_uploaded_file($tmpFileName)) {
    // Получаем оригинальное имя файла
    $originalName = $_FILES['uploaded_file']['name'];
    
    // Генерация уникального имени для сохранения
    $uniqueName = uniqid() . '_' . $originalName;
    $destinationPath = '/var/www/html/uploads/' . $uniqueName;

    // Перемещение временного файла в постоянное хранилище
    if (move_uploaded_file($tmpFileName, $destinationPath)) {
        echo "Файл успешно сохранен как: {$uniqueName}\n";
        
        // Здесь может быть долгая операция, например, конвертация изображения
        
        // После завершения операций временный файл уже перемещен, 
        // но если мы создавали свой temp-файл через tmpfile(), нужно удалить его:
        
        // Пример создания и удаления своего временного файла
        $tempHandle = tmpfile();
        fwrite($tempHandle, "Временные данные\n");
        fclose($tempHandle); // Временный файл удаляется автоматически при закрытии handle
        
        // Или использование tempnam для получения пути к временному файлу
        $tempPath = tempnam(sys_get_temp_dir(), 'myapp_');
        file_put_contents($tempPath, "Данные для обработки");
        
        // Явное удаление после обработки
        unlink($tempPath);
        echo "Временный файл удален вручную.\n";
        
    } else {
        echo "Ошибка при перемещении файла.\n";
    }
} else {
    echo "Файл не был загружен.\n";
}
?>
