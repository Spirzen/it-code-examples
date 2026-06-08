var table = new TableLayoutPanel
{
    Dock = DockStyle.Fill,
    Padding = new Padding(12),
    ColumnCount = 2,
    RowCount = 3
};
table.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
table.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100f));

var emailBox = new TextBox { Dock = DockStyle.Fill, Margin = new Padding(8, 4, 0, 4) };
var passBox = new TextBox
{
    Dock = DockStyle.Fill,
    UseSystemPasswordChar = true,
    Margin = new Padding(8, 4, 0, 4)
};
var loginButton = new Button { Text = "Войти", Anchor = AnchorStyles.Right, AutoSize = true };
loginButton.Click += (_, _) => MessageBox.Show("Вход (демо)");

table.Controls.Add(new Label { Text = "Email:", AutoSize = true }, 0, 0);
table.Controls.Add(emailBox, 1, 0);
table.Controls.Add(new Label { Text = "Пароль:", AutoSize = true }, 0, 1);
table.Controls.Add(passBox, 1, 1);
table.Controls.Add(loginButton, 1, 2);

form.Controls.Add(table);
