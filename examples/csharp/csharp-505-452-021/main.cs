[Fact]
public void GetProduct_ReturnsNotFound_WhenProductIsNull()
{
    // Arrange
    var mockRepo = new Mock<IProductRepository>();
    mockRepo.Setup(r => r.GetByIdAsync(1)).ReturnsAsync((Product)null);
    var controller = new ProductsController(mockRepo.Object);

    // Act
    var result = controller.GetProduct(1);

    // Assert
    Assert.IsType<NotFoundResult>(result.Result);
}
