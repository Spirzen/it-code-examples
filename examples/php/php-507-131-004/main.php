<?php
/**
 * Трекер задач с сохранением в JSON
 * 
 * Команды:
 * - add <задача>: Добавить новую задачу
 * - list: Показать все задачи
 * - clear: Очистить список
 */

$dataFile = 'Задачи.json';
$Задачи = [];

// Загрузка существующих данных
if (file_exists($dataFile)) {
    $content = file_get_contents($dataFile);
    $Задачи = json_decode($content, true) ?: [];
}

$command = $argv[1] ?? '';
$taskText = $argv[2] ?? '';

switch ($command) {
    case 'add':
        if (empty($taskText)) {
            echo "Ошибка: Укажите текст задачи.\n";
            exit(1);
        }
        $newTask = [
            'id' => uniqid(),
            'text' => $taskText,
            'created_at' => date('Y-m-d H:i:s')
        ];
        $Задачи[] = $newTask;
        saveTasks($Задачи);
        echo "Задача добавлена.\n";
        break;

    case 'list':
        if (empty($Задачи)) {
            echo "Список задач пуст.\n";
        } else {
            echo "Список задач:\n";
            foreach ($Задачи as $task) {
                echo "- [{$task['id']}] {$task['text']} (создано: {$task['created_at']})\n";
            }
        }
        break;

    case 'clear':
        $Задачи = [];
        saveTasks($Задачи);
        echo "Список задач очищен.\n";
        break;

    default:
        echo "Неизвестная команда. Используйте: add, list, clear\n";
        break;
}

function saveTasks(array $Задачи): void {
    global $dataFile;
    $jsonContent = json_encode($Задачи, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    file_put_contents($dataFile, $jsonContent);
}
?>
