<?php
// Определение трейта с методом логирования
trait Loggable {
    public function log(string $message): void {
        echo "[LOG] {$message}\n";
    }
}

// Определение другого трейта с таким же именем метода
trait Timestampable {
    public function log(string $message): void {
        echo "[TIMESTAMP] {$message} at " . date('Y-m-d H:i:s') . "\n";
    }
}

// Класс, использующий оба трейта
class OrderService {
    use Loggable, Timestampable {
        // Разрешаем конфликт: метод из Timestampable имеет приоритет
        Timestampable::log insteadof Loggable;
        // Или можно создать алиас для оригинального метода Loggable
        // Loggable::log as logClassic;
    }

    public function createOrder(): void {
        // Вызовется метод из Timestampable
        $this->log("Создание заказа...");
    }
}

$service = new OrderService();
$service->createOrder();
// Вывод: [TIMESTAMP] Создание заказа... at ...
