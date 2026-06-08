using Microsoft.AspNetCore.Mvc;
using StoreMvc.Services;

namespace StoreMvc.Controllers;

public class HomeController : Controller
{
    private readonly IProductRepository _products;

    public HomeController(IProductRepository products) => _products = products;

    public IActionResult Index()
    {
        var list = _products.GetAll();
        return View(list);
    }
}
