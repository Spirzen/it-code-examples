class DatabaseConnection {
    private $pdo;
    private string $dsn;

    public function __construct(string $dsn) {
        $this->dsn = $dsn;
        $this->pdo = new PDO($dsn);
    }

    public function __sleep(): array {
        return ['dsn']; // сохраняем только DSN
    }

    public function __wakeup(): void {
        $this->pdo = new PDO($this->dsn); // восстанавливаем соединение
    }
}
