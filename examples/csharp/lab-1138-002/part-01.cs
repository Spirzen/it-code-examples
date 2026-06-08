using System.Drawing;
using System.Windows.Forms;

namespace HelloWinForms;

static class Program
{
    [STAThread]
    static void Main()
    {
        ApplicationConfiguration.Initialize();

        var form = new Form
        {
            Text = "Привет, WinForms",
            ClientSize = new Size(400, 200),
            StartPosition = FormStartPosition.CenterScreen
        };

        var label = new Label
        {
            Text = "Окно работает!",
            AutoSize = true,
            Location = new Point(20, 20),
            Font = new Font("Segoe UI", 14f)
        };
        form.Controls.Add(label);

        Application.Run(form);
    }
}
