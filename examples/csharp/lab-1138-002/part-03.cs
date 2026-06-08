using System.Drawing;
using System.Windows.Forms;

namespace GreetApp;

static class Program
{
    [STAThread]
    static void Main()
    {
        ApplicationConfiguration.Initialize();

        var form = new Form
        {
            Text = "Приветствие",
            ClientSize = new Size(360, 160),
            StartPosition = FormStartPosition.CenterScreen,
            FormBorderStyle = FormBorderStyle.FixedDialog,
            MaximizeBox = false
        };

        var nameLabel = new Label
        {
            Text = "Ваше имя:",
            AutoSize = true,
            Location = new Point(20, 24)
        };

        var entry = new TextBox
        {
            Location = new Point(120, 20),
            Width = 200
        };

        var greetButton = new Button
        {
            Text = "Приветствовать",
            Location = new Point(20, 60),
            AutoSize = true
        };

        greetButton.Click += (_, _) =>
        {
            var name = entry.Text.Trim();
            if (string.IsNullOrEmpty(name))
            {
                MessageBox.Show("Введите имя", "Пусто",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            MessageBox.Show($"Здравствуй, {name}!", "Привет");
        };

        form.Controls.Add(nameLabel);
        form.Controls.Add(entry);
        form.Controls.Add(greetButton);
        entry.Focus();

        Application.Run(form);
    }
}
