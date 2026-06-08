public class TaskListViewModelTests
{
    [Fact]
    public async Task AddTask_WithEmptyTitle_DoesNotCallRepository()
    {
        var repo = new Mock<ITaskRepository>();
        var vm = new TaskListViewModel(repo.Object) { NewTitle = "   " };

        await vm.AddTaskCommand.ExecuteAsync(null);

        repo.Verify(r => r.CreateAsync(It.IsAny<TaskItem>(), default), Times.Never);
    }

    [Fact]
    public async Task AddTask_ValidTitle_CallsRepositoryAndClearsTitle()
    {
        var repo = new Mock<ITaskRepository>();
        repo.Setup(r => r.CreateAsync(It.IsAny<TaskItem>(), default))
            .ReturnsAsync((TaskItem t, CancellationToken _) => t);

        var vm = new TaskListViewModel(repo.Object) { NewTitle = "Deploy" };
        await vm.AddTaskCommand.ExecuteAsync(null);

        repo.Verify(r => r.CreateAsync(It.Is<TaskItem>(x => x.Title == "Deploy"), default), Times.Once);
        Assert.Equal("", vm.NewTitle);
    }
}
