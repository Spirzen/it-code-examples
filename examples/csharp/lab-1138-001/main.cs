using System.Drawing;
using System.Windows.Forms;

namespace MyDesktopApp;

static class Program
{
    [STAThread]
    static void Main()
    {
        ApplicationConfiguration.Initialize();

        var form = new Form
        {
            Text = "Моё приложение",
            ClientSize = new Size(400, 300),
            StartPosition = FormStartPosition.CenterScreen
        };

        // --- здесь Label, Button, TextBox и остальные контролы ---

        Application.Run(form);
    }
}
