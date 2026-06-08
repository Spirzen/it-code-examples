<?php
/**
 * Класс-обёртка для конфигурации, эмулирующий поведение массива.
 */
class Config implements ArrayAccess {
    private array $data = [];

    public function __construct(array $initialData) {
        $this->data = $initialData;
    }

    // Обязательные методы для реализации ArrayAccess

    public function offsetExists(mixed $offset): bool {
        return isset($this->data[$offset]);
    }

    public function offsetGet(mixed $offset): mixed {
        return $this->data[$offset] ?? null;
    }

    public function offsetSet(mixed $offset, mixed $value): void {
        if (is_null($offset)) {
            $this->data[] = $value;
        } else {
            $this->data[$offset] = $value;
        }
    }

    public function offsetUnset(mixed $offset): void {
        unset($this->data[$offset]);
    }
}

// Пример использования
$config = new Config(['host' => 'localhost', 'port' => 3306]);

// Синтаксис массива работает
echo $config['host']; // Вывод: localhost
$config['user'] = 'admin';

// Но is_array() вернет false, так как это объект
var_dump(is_array($config)); // Вывод: bool(false)
