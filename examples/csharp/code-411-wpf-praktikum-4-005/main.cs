[ObservableProperty]
private string? _errorMessage;

[RelayCommand]
private async Task LoadTasksAsync()
{
    ErrorMessage = null;
    IsBusy = true;
    try
    {
        var items = await _repository.GetAllAsync();
        Tasks.Clear();
        foreach (var t in items)
            Tasks.Add(TaskItemViewModel.FromModel(t));
    }
    catch (HttpRequestException ex)
    {
        ErrorMessage = "Сервер недоступен. Запустите TaskDesk.Api на порту 5100.";
        // лог: ex.Message
    }
    finally
    {
        IsBusy = false;
    }
}
