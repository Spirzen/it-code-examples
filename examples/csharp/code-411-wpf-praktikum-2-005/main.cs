[ObservableProperty]
private bool _isBusy;

[RelayCommand]
private async Task LoadTasksAsync()
{
    if (IsBusy) return;
    IsBusy = true;
    try
    {
        var items = await _repository.GetAllAsync();
        Tasks.Clear();
        foreach (var t in items)
            Tasks.Add(TaskItemViewModel.FromModel(t));
    }
    finally
    {
        IsBusy = false;
    }
}
