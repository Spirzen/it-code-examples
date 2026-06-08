interface ContainerInterface {
    public function get(string $id);
    public function has(string $id): bool;
}

class Container implements ContainerInterface
{
    private array $definitions = [];
    private array $instances = [];

    public function set(string $id, callable $factory): void
    {
        $this->definitions[$id] = $factory;
    }

    public function get(string $id)
    {
        if (isset($this->instances[$id])) {
            return $this->instances[$id];
        }
        if (!isset($this->definitions[$id])) {
            throw new Exception("Entry '$id' not found");
        }
        return $this->instances[$id] = ($this->definitions[$id])($this);
    }

    public function has(string $id): bool
    {
        return isset($this->definitions[$id]);
    }
}

// Использование
$container = new Container();
$container->set('pdo', fn() => new PDO('sqlite::memory:'));
$container->set('userRepository', fn($c) => new UserRepository($c->get('pdo')));

$userRepo = $container->get('userRepository');
