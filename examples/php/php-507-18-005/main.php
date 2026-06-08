interface Logger {
    public function log(string $message): void;
}

class FileLogger implements Logger {
    public function log(string $message): void {
        file_put_contents('log.txt', $message . PHP_EOL, FILE_APPEND);
    }
}

class ConsoleLogger implements Logger {
    public function log(string $message): void {
        echo "[LOG] $message\n";
    }
}
