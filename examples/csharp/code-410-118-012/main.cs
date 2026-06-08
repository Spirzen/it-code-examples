// Пример тестирования с In-Memory базой данных
[Fact]
public async Task GetUserById_ReturnsUser_WhenUserExists()
{
    var options = new DbContextOptionsBuilder<AppDbContext>()
        .UseInMemoryDatabase(databaseName: "TestDatabase")
        .Options;
    
    using (var context = new AppDbContext(options))
    {
        // Подготовка данных
        var user = new User { Id = 1, Name = "Иван" };
        context.Users.Add(user);
        await context.SaveChangesAsync();
        
        // Выполнение теста
        var result = await context.Users.FindAsync(1);
        
        // Проверка результата
        Assert.NotNull(result);
        Assert.Equal("Иван", result.Name);
    }
}

// Пример тестирования с моками
[Fact]
public async Task ProcessOrder_CallsRepositoryMethods_Correctly()
{
    var mockContext = new Mock<AppDbContext>();
    var mockSet = new Mock<DbSet<User>>();
    
    mockContext.Setup(x => x.Users).Returns(mockSet.Object);
    
    var repository = new UserRepository(mockContext.Object);
    var user = new User { Id = 1, Name = "Иван" };
    
    await repository.GetByIdAsync(1);
    
    mockContext.Verify(x => x.Users.FindAsync(1), Times.Once);
}
