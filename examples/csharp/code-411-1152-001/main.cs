var textBox = new TextBox
{
    Width = 240,
    PlaceholderText = "Введите имя"  // .NET 6+
};
table.Controls.Add(textBox, 1, 0);

string value = textBox.Text.Trim();
textBox.Clear();
textBox.Text = "по умолчанию";

textBox.KeyDown += (s, e) =>
{
    if (e.KeyCode == Keys.Enter) Submit();
};
