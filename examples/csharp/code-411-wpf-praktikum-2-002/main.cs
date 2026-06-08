public class TaskListViewModel : INotifyPropertyChanged
{
    public event PropertyChangedEventHandler? PropertyChanged;

    private string _newTitle = "";
    public string NewTitle
    {
        get => _newTitle;
        set
        {
            if (_newTitle == value) return;
            _newTitle = value;
            PropertyChanged?.Invoke(this, new(nameof(NewTitle)));
            AddTaskCommand.RaiseCanExecuteChanged();
        }
    }

    public ObservableCollection<TaskItemViewModel> Tasks { get; } = new();
    public RelayCommand AddTaskCommand { get; }

    public TaskListViewModel(ITaskRepository repository)
    {
        _repository = repository;
        AddTaskCommand = new RelayCommand(ExecuteAdd, CanAdd);
    }
}
