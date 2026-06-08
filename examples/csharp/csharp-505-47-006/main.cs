public class ProductsController : ControllerBase
{
    private readonly IProductRepository _repository;
    private readonly IDistributedCache _cache;

    public ProductsController(IProductRepository repository, IDistributedCache cache)
    {
        _repository = repository;
        _cache = cache;
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Product>> GetProduct(int id)
    {
        // ... кэширование
        var product = await _repository.GetByIdAsync(id);
        // ... сериализация и сохранение в кэш
    }
}
