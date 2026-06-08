[Fact]
public async Task GetByIdAsync_ExistingId_ReturnsProduct()
{
    // Arrange
    var mockContext = new Mock<AppDbContext>();
    var mockSet = new Mock<DbSet<Product>>();
    mockSet.Setup(s => s.FindAsync(1))
           .ReturnsAsync(new Product { Id = 1, Name = "Тест", Price = 100 });
    mockContext.Setup(c => c.Products).Returns(mockSet.Object);

    var repo = new ProductRepository(mockContext.Object);

    // Act
    var result = await repo.GetByIdAsync(1);

    // Assert
    Assert.NotNull(result);
    Assert.Equal("Тест", result.Name);
}
