class UserManager {
    private Logger $logger;

    public function __construct(Logger $logger) {
        $this->logger = $logger;
    }

    public function createUser(string $name): void {
        // … логика создания
        $this->logger->log("Создан пользователь: $name");
    }
}

// Гибкая компоновка:
$manager = new UserManager(new FileLogger());
// или
$manager = new UserManager(new ConsoleLogger());
