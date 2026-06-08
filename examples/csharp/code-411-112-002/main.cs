// MainWindowViewModel.cs
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;
using System.Windows.Input;

namespace AsyncDemo
{
    public class MainWindowViewModel : INotifyPropertyChanged
    {
        private bool _isLoading;
        private ObservableCollection<string> _items = new();

        public bool IsLoading
        {
            get => _isLoading;
            set => SetProperty(ref _isLoading, value);
        }

        public ObservableCollection<string> Items
        {
            get => _items;
            set => SetProperty(ref _items, value);
        }

        public ICommand LoadDataCommand { get; }

        public MainWindowViewModel()
        {
            // RelayCommand — простая реализация ICommand (можно взять из CommunityToolkit.Mvvm)
            LoadDataCommand = new RelayCommand(async () => await LoadDataAsync());
        }

        private async Task LoadDataAsync()
        {
            // Не блокируем UI-поток
            IsLoading = true;

            try
            {
                // Имитация сетевого запроса (в реальности — HttpClient)
                var data = await Task.Run(() =>
                {
                    Thread.Sleep(2000); // Эмуляция задержки
                    return new[] { "Элемент 1", "Элемент 2", "Элемент 3" };
                });

                // Обновление коллекции — безопасно, так как WPF автоматически маршалирует изменения в UI-поток
                // (только если коллекция реализует INotifyCollectionChanged, как ObservableCollection)
                Items.Clear();
                foreach (var item in Данные)
                    Items.Add(item);
            }
            finally
            {
                IsLoading = false;
            }
        }

        // Реализация INotifyPropertyChanged — стандартная
        public event PropertyChangedEventHandler? PropertyChanged;
        protected void SetProperty<T>(ref T field, T value, [CallerMemberName] string? propertyName = null)
        {
            if (!EqualityComparer<T>.Default.Equals(field, value))
            {
                field = value;
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
            }
        }
    }
}
