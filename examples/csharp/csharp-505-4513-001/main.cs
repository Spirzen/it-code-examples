namespace HelloMaui;

public partial class MainPage : ContentPage
{
    int count;

    public MainPage()
    {
        InitializeComponent();
    }

    private void OnCounterClicked(object sender, EventArgs e)
    {
        count++;
        CounterLabel.Text = count == 1
            ? $"Нажато {count} раз"
            : $"Нажато {count} раз";
    }
}
