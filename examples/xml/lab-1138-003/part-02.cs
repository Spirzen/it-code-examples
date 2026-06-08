using System.Windows;

namespace GreetApp;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        NameBox.Focus();
    }

    private void OnGreet(object sender, RoutedEventArgs e)
    {
        var name = NameBox.Text.Trim();
        if (string.IsNullOrEmpty(name))
        {
            MessageBox.Show("Введите имя", "Пусто",
                MessageBoxButton.OK, MessageBoxImage.Warning);
            return;
        }
        MessageBox.Show($"Здравствуй, {name}!", "Привет");
    }
}
