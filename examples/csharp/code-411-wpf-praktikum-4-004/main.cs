public partial class TaskListViewModel : ObservableObject, INavigationAware
{
    private readonly ITaskRepository _repository;

    public TaskListViewModel(ITaskRepository repository) =>
        _repository = repository;

    public async void OnNavigatedTo(NavigationContext navigationContext) =>
        await LoadTasksCommand.ExecuteAsync(null);

    public void OnNavigatedFrom(NavigationContext navigationContext) { }

    public bool IsNavigationTarget(NavigationContext navigationContext) => true;
}
