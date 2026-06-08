interface LoggerInterface
{
    public function log($message);
}

class FileLogger implements LoggerInterface
{
    public function log($message)
    {
        file_put_contents('log.txt', $message . PHP_EOL, FILE_APPEND);
    }
}

class CacheLogger implements LoggerInterface
{
    protected $logger;

    public function __construct(LoggerInterface $logger)
    {
        $this->logger = $logger;
    }

    public function log($message)
    {
        // Логика кэширования перед записью
        $this->logger->log($message);
        // Логика после записи
    }
}
