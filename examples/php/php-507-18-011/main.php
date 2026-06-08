class Config {
    private array $data = [];

    public function __set(string $key, $value): void {
        $this->data[$key] = $value;
    }

    public function __get(string $key) {
        return $this->data[$key] ?? null;
    }
}

$config = new Config();
$config->database = 'mysql'; // → вызов __set('database', 'mysql')
echo $config->database;       // → вызов __get('database')
