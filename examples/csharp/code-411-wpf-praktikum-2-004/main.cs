public partial class TaskListViewModel : ObservableObject
{
    private readonly ITaskRepository _repository;

    [ObservableProperty]
    private string _newTitle = "";

    public ObservableCollection<TaskItemViewModel> Tasks { get; } = new();

    [RelayCommand(CanExecute = nameof(CanAddTask))]
    private async Task AddTaskAsync()
    {
        var item = new TaskItem { Title = NewTitle.Trim() };
        await _repository.CreateAsync(item);
        Tasks.Add(TaskItemViewModel.FromModel(item));
        NewTitle = "";
    }

    private bool CanAddTask() => !string.IsNullOrWhiteSpace(NewTitle);
}
