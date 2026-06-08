using System.Drawing;
using System.Globalization;
using System.Windows.Forms;

namespace TempConverter;

static class Program
{
    [STAThread]
    static void Main()
    {
        ApplicationConfiguration.Initialize();

        var form = new Form
        {
            Text = "Конвертер температуры",
            ClientSize = new Size(340, 180),
            StartPosition = FormStartPosition.CenterScreen,
            FormBorderStyle = FormBorderStyle.FixedDialog,
            MaximizeBox = false
        };

        var tempLabel = new Label
        {
            Text = "Температура (°C):",
            AutoSize = true,
            Location = new Point(20, 24)
        };

        var entry = new TextBox { Location = new Point(160, 20), Width = 80 };

        var resultLabel = new Label
        {
            Text = "—",
            AutoSize = true,
            Location = new Point(20, 60),
            Font = new Font("Segoe UI", 12f)
        };

        var convertButton = new Button
        {
            Text = "Перевести",
            Location = new Point(20, 100),
            AutoSize = true
        };

        convertButton.Click += (_, _) =>
        {
            var raw = entry.Text.TrimReplace(',', '.');
            if (!double.TryParse(raw, NumberStyles.Any, CultureInfo.InvariantCulture, out var celsius))
            {
                MessageBox.Show("Введите число, например 25", "Ошибка");
                return;
            }
            var fahrenheit = celsius * 9 / 5 + 32;
            resultLabel.Text = $"{celsius:F1} °C = {fahrenheit:F1} °F";
        };

        entry.KeyDown += (_, e) =>
        {
            if (e.KeyCode == Keys.Enter)
                convertButton.PerformClick();
        };

        form.Controls.Add(tempLabel);
        form.Controls.Add(entry);
        form.Controls.Add(resultLabel);
        form.Controls.Add(convertButton);
        entry.Focus();

        Application.Run(form);
    }
}
