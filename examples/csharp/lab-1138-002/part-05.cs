using System.Drawing;
using System.Windows.Forms;

namespace TodoList;

static class Program
{
    [STAThread]
    static void Main()
    {
        ApplicationConfiguration.Initialize();

        var form = new Form
        {
            Text = "Список задач",
            ClientSize = new Size(320, 280),
            StartPosition = FormStartPosition.CenterScreen
        };

        var entry = new TextBox { Location = new Point(12, 12), Width = 280 };
        var addButton = new Button { Text = "Добавить", Location = new Point(12, 44), AutoSize = true };
        var removeButton = new Button { Text = "Удалить", Location = new Point(100, 44), AutoSize = true };
        var listBox = new ListBox { Location = new Point(12, 80), Size = new Size(280, 160) };

        void AddTask()
        {
            var text = entry.Text.Trim();
            if (text.Length == 0) return;
            listBox.Items.Add(text);
            entry.Clear();
        }

        void RemoveTask()
        {
            if (listBox.SelectedIndex >= 0)
                listBox.Items.RemoveAt(listBox.SelectedIndex);
        }

        addButton.Click += (_, _) => AddTask();
        removeButton.Click += (_, _) => RemoveTask();
        entry.KeyDown += (_, e) => { if (e.KeyCode == Keys.Enter) AddTask(); };

        form.Controls.AddRange(new Control[] { entry, addButton, removeButton, listBox });
        entry.Focus();

        Application.Run(form);
    }
}
