[HttpGet("{id}")]
public async Task<ActionResult<Product>> GetProduct(int id)
{
    var redis = HttpContext.RequestServices.GetRequiredService<IConnectionMultiplexer>();
    var cache = redis.GetDatabase();

    var cached = await cache.StringGetAsync($"product:{id}");
    if (!cached.IsNullOrEmpty)
    {
        var product = JsonSerializer.Deserialize<Product>(cached!);
        return Ok(product);
    }

    var product = await _context.Products.FindAsync(id);
    if (product == null)
        return NotFound();

    var json = JsonSerializer.Serialize(product);
    await cache.StringSetAsync($"product:{id}", json, TimeSpan.FromMinutes(10));

    return product;
}
