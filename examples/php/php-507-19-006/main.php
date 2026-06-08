<?php
class User
{
    private string $firstName = '';
    private string $lastName = '';
    private array $meta = [];

    // Ленивая инициализация свойства
    public function __get(string $name): mixed {
        if ($name === 'fullName') {
            return "{$this->firstName} {$this->lastName}";
        }
        
        // Доступ к метаданным через маппинг
        if (isset($this->meta[$name])) {
            return $this->meta[$name];
        }

        throw new \Exception("Свойство '{$name}' не найдено");
    }

    // Динамические методы поиска
    public function __call(string $name, array $arguments): mixed {
        // Метод findByEmail
        if (str_starts_with($name, 'findBy')) {
            $field = lcfirst(substr($name, 6)); // превращаем Email -> email
            // Имитация запроса к БД
            return ["id" => 1, $field => $arguments[0]]; 
        }

        throw new \BadMethodCallException("Метод {$name} не существует");
    }
}

$user = new User();
$user->firstName = 'Алексей';
$user->lastName = 'Петров';

// Доступ к несуществующему свойству fullName
echo $user->fullName . "\n"; // Алексей Петров

// Вызов динамического метода
$result = $user->findByEmail('alex@test.ru');
print_r($result);
// Array ( [id] => 1 [email] => alex@test.ru )
