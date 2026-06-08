[ApiController]
[ApiVersion("1.0")]
[ApiVersion("2.0")]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    [HttpGet]
    [MapToApiVersion("2.0")] // только для v2
    public IActionResult GetV2() => Ok("v2");

    [HttpGet]
    [MapToApiVersion("1.0")] // только для v1
    public IActionResult GetV1() => Ok("v1");
}
