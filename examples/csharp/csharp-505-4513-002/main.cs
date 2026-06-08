public partial class NotesViewModel : ObservableObject
{
    [ObservableProperty]
    private string newText = "";

    public ObservableCollection<string> Notes { get; } = new();

    [RelayCommand]
    private void Add()
    {
        if (string.IsNullOrWhiteSpace(NewText)) return;
        Notes.Add(NewText.Trim());
        NewText = "";
    }
}
