var aBox = new TextBox { Location = new Point(20, 20), Width = 60 };
var bBox = new TextBox { Location = new Point(100, 20), Width = 60 };
var sumButton = new Button { Text = "=", Location = new Point(180, 18), AutoSize = true };
var resultLabel = new Label { Location = new Point(220, 22), AutoSize = true };

sumButton.Click += (_, _) =>
{
    if (double.TryParse(aBox.Text.Replace(',', '.'), out var a) &&
        double.TryParse(bBox.Text.Replace(',', '.'), out var b))
        resultLabel.Text = (a + b).ToString("G");
    else
        resultLabel.Text = "Ошибка";
};

form.Controls.AddRange(new Control[] { aBox, bBox, sumButton, resultLabel });
