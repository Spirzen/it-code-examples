[Fact]
public async Task IssueBook_WhenBookIsAvailable_ShouldCreateLoan()
{
    // Arrange
    var context = CreateInMemoryDbContext();
    var service = new LoanService(context);
    
    // Act
    var result = await service.IssueBookAsync(bookId: 1, readerId: 1);
    
    // Assert
    Assert.True(result.IsSuccess);
    Assert.Single(context.Loans);
}
