Button applyButton = new Button("Применить");
applyButton.setDefaultButton(true);
applyButton.setOnAction(e -> {
    String date = datePicker.getValue() != null
            ? datePicker.getValue().format(DateTimeFormatter.ofPattern("dd.MM.yyyy"))
            : "—";
    status.setText(String.format(
            "Форма: %s | роль %s | дата %s | громкость %.0f%% | уведомления %s | тема %s",
            nameField.getText().isBlank() ? "(без имени)" : nameField.getText(),
            roleBox.getValue(),
            date,
            volumeSlider.getValue(),
            notifyCheck.isSelected() ? "вкл" : "выкл",
            lightTheme.isSelected() ? "светлая" : "тёмная"
    ));
});
