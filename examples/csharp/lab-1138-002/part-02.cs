using System.Drawing;
using System.Windows.Forms;

namespace ButtonDemo;

static class Program
{
    [STAThread]
    static void Main()
    {
        ApplicationConfiguration.Initialize();

        var form = new Form
        {
            Text = "Кнопка",
            ClientSize = new Size(320, 180),
            StartPosition = FormStartPosition.CenterScreen
        };

        var button = new Button
        {
            Text = "Нажми меня",
            Location = new Point(20, 20),
            AutoSize = true
        };

        // Click += подписка на событие; лямбда вызывается ТОЛЬКО по клику
        button.Click += (_, _) => MessageBox.Show(
            "Кнопка нажата!",
            "Сообщение",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information);

        form.Controls.Add(button);
        Application.Run(form);
    }
}
