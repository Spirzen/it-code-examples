trait Loggable {
    public function log(string $msg): void {
        error_log("[LOG] $msg");
    }
}

class Service {
    use Loggable;

    public function process(): void {
        $this->log("Начата обработка");
        // … основная логика
        $this->log("Обработка завершена");
    }
}
