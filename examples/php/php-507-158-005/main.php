#[\Attribute(\Attribute::TARGET_METHOD)]
class Route
{
    public function __construct(
        public string $path,
        public array $methods = ['GET'],
    ) {}
}

class HomeController
{
    #[Route('/')]
    public function index(): string
    {
        return 'Главная';
    }

    #[Route('/about', methods: ['GET'])]
    public function about(): string
    {
        return 'О проекте';
    }
}
