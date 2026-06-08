using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;
using NoteKeeper.Models;

namespace NoteKeeper.ViewModels;

public sealed class MainViewModel : INotifyPropertyChanged
{
    private string _newTitle = string.Empty;
    private string _selectedCategory = "Работа";

    public string NewTitle
    {
        get => _newTitle;
        set => SetProperty(ref _newTitle, value);
    }

    public string SelectedCategory
    {
        get => _selectedCategory;
        set => SetProperty(ref _selectedCategory, value);
    }

    public ObservableCollection<string> Categories { get; } =
        new(["Работа", "Личное", "Идеи"]);

    public ObservableCollection<NoteItem> Notes { get; } = new();

    public ICommand AddNoteCommand { get; }

    public MainViewModel()
    {
        AddNoteCommand = new RelayCommand(AddNote, () => !string.IsNullOrWhiteSpace(NewTitle));
    }

    private void AddNote()
    {
        Notes.Add(new NoteItem
        {
            Title = NewTitle.Trim(),
            Category = SelectedCategory,
        });
        NewTitle = string.Empty;
        ((RelayCommand)AddNoteCommand).RaiseCanExecuteChanged();
    }

    public event PropertyChangedEventHandler? PropertyChanged;

    private void SetProperty<T>(ref T field, T value, [CallerMemberName] string? name = null)
    {
        if (EqualityComparer<T>.Default.Equals(field, value)) return;
        field = value;
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        if (name == nameof(NewTitle))
            ((RelayCommand)AddNoteCommand).RaiseCanExecuteChanged();
    }
}

internal sealed class RelayCommand : ICommand
{
    private readonly Action _execute;
    private readonly Func<bool>? _canExecute;

    public RelayCommand(Action execute, Func<bool>? canExecute = null)
    {
        _execute = execute;
        _canExecute = canExecute;
    }

    public event EventHandler? CanExecuteChanged;

    public bool CanExecute(object? parameter) => _canExecute?.Invoke() ?? true;

    public void Execute(object? parameter) => _execute();

    public void RaiseCanExecuteChanged() =>
        CanExecuteChanged?.Invoke(this, EventArgs.Empty);
}
