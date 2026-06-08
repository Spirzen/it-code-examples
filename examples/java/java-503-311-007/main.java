
package com.example;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class HelloController {

    @FXML
    private TextField celsiusField;

    @FXML
    private Label resultLabel;

    @FXML
    private void convert() {
        try {
            double c = Double.parseDouble(celsiusField.getText().trim().replace(',', '.'));
            double f = c * 9 / 5 + 32;
            resultLabel.setText(String.format("%.1f °C = %.1f °F", c, f));
        } catch (NumberFormatException ex) {
            resultLabel.setText("Введите число");
        }
    }
}
