var notifyCheck = new CheckBox
{
    Text = "Уведомления", Location = new Point(20, 20), Checked = true, AutoSize = true
};
var soundCheck = new CheckBox { Text = "Звук", Location = new Point(20, 50), AutoSize = true };
var userRadio = new RadioButton
{
    Text = "Пользователь", Location = new Point(20, 90), Checked = true, AutoSize = true
};
var adminRadio = new RadioButton { Text = "Администратор", Location = new Point(20, 120), AutoSize = true };
var statusLabel = new Label { Location = new Point(20, 160), AutoSize = true, ForeColor = Color.Gray };

void UpdateStatus()
{
    var parts = new List<string>();
    if (notifyCheck.Checked) parts.Add("уведомления");
    if (soundCheck.Checked) parts.Add("звук");
    var role = adminRadio.Checked ? "admin" : "user";
    statusLabel.Text = $"Роль: {role}; включено: {(parts.Count > 0 ? string.Join(", ", parts) : "ничего")}";
}

notifyCheck.CheckedChanged += (_, _) => UpdateStatus();
soundCheck.CheckedChanged += (_, _) => UpdateStatus();
userRadio.CheckedChanged += (_, _) => UpdateStatus();
adminRadio.CheckedChanged += (_, _) => UpdateStatus();

form.Controls.AddRange(new Control[] { notifyCheck, soundCheck, userRadio, adminRadio, statusLabel });
UpdateStatus();
