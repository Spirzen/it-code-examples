<?php
// Веб-запрос: создание задачи и её помещение в "очередь" (в примере — в массив/файл)
class EmailTask {
    public string $to;
    public string $subject;
    public string $body;
    public string $taskId;

    public function __construct(string $to, string $subject, string $body) {
        $this->to = $to;
        $this->subject = $subject;
        $this->body = $body;
        $this->taskId = uniqid('task_');
    }

    public function toJson(): string {
        return json_encode([
            'type' => 'send_email',
            'id' => $this->taskId,
            'Данные' => get_object_vars($this)
        ]);
    }
}

// Эмуляция веб-запроса
$task = new EmailTask('client@example.com', 'Заказ оформлен', 'Ваш заказ #123 принят');
$queueFile = 'queue.json';

// Сохранение в "очередь" (в реальности здесь был бы push в Redis/RabbitMQ)
$currentQueue = file_exists($queueFile) ? json_decode(file_get_contents($queueFile), true) : [];
$currentQueue[] = $task->toJson();
file_put_contents($queueFile, json_encode($currentQueue, JSON_PRETTY_PRINT));

echo "Задача создана с ID: {$task->taskId}. Она будет обработана фоновым воркером.\n";

/*
 * Воркер (отдельный процесс) читает этот файл, берет задачу, выполняет отправку почты
 * и удаляет запись из очереди. Это гарантирует, что веб-сервер не ждет окончания отправки.
 */
