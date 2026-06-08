interface RequestHandlerInterface {
    public function handle(ServerRequestInterface $request): ResponseInterface;
}

interface MiddlewareInterface {
    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface;
}

class LoggingMiddleware implements MiddlewareInterface
{
    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
    {
        $start = microtime(true);
        $response = $handler->handle($request);
        $duration = microtime(true) - $start;
        error_log("{$request->getMethod()} {$request->getUri()->getPath()} — {$duration}s");
        return $response;
    }
}

class Dispatcher
{
    public function dispatch(array $middlewareStack, ServerRequestInterface $request): ResponseInterface
    {
        $next = new class($middlewareStack) implements RequestHandlerInterface {
            private int $index = 0;

            public function __construct(private array $stack) {}

            public function handle(ServerRequestInterface $request): ResponseInterface
            {
                if ($this->index >= count($this->stack)) {
                    return new Response(200); // default
                }
                $middleware = $this->stack[$this->index++];
                return $middleware->process($request, $this);
            }
        };

        return $next->handle($request);
    }
}
