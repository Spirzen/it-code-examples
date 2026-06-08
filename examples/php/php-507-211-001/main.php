class Router
{
    private array $routes = [];

    public function add(string $method, string $pattern, callable $handler): void
    {
        $this->routes[] = [$method, $pattern, $handler];
    }

    public function dispatch(string $method, string $uri): void
    {
        foreach ($this->routes as [$m, $pattern, $handler]) {
            if ($m !== $method) continue;

            $pattern = preg_quote($pattern, '#');
            $pattern = preg_replace('#\{(\w+)\}#', '(?P<$1>[^/]+)', $pattern);
            $pattern = '#^' . $pattern . '$#u';

            if (preg_match($pattern, $uri, $matches)) {
                $params = array_filter($matches, 'is_string', ARRAY_FILTER_USE_KEY);
                $handler($params);
                return;
            }
        }
        http_response_code(404);
        echo "Not found";
    }
}

// Использование
$router = new Router();
$router->add('GET', '/users/{id}', function ($params) {
    echo "User ID: " . htmlspecialchars($params['id']);
});
$router->dispatch($_SERVER['REQUEST_METHOD'], parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));
