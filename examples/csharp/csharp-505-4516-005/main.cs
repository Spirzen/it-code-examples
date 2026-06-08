using Microsoft.AspNetCore.Mvc;
using Moq;
using StoreMvc.Controllers;
using StoreMvc.Services;

namespace StoreMvc.Tests;

public class HomeControllerTests
{
    [Fact]
    public void Index_ReturnsView_WithProductsFromRepository()
    {
        var data = new List<Product>
        {
            new(1, "Мяч", 499m),
            new(2, "Сетка", 199m)
        };

        var repo = new Mock<IProductRepository>();
        repo.Setup(r => r.GetAll()).Returns(data);

        var controller = new HomeController(repo.Object);

        var result = controller.Index();

        var view = Assert.IsType<ViewResult>(result);
        var model = Assert.IsAssignableFrom<IReadOnlyList<Product>>(view.Model);
        Assert.Equal(2, model.Count);
        Assert.Equal("Мяч", model[0].Name);
        repo.Verify(r => r.GetAll(), Times.Once);
    }
}
