
package com.example;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class ConverterApp extends Application {

    private TextField celsiusField;
    private Label resultLabel;

    private void convert() {
        String raw = celsiusField.getText().trim().replace(',', '.');
        try {
            double celsius = Double.parseDouble(raw);
            double fahrenheit = celsius * 9 / 5 + 32;
            resultLabel.setText(String.format("%.1f °C = %.1f °F", celsius, fahrenheit));
        } catch (NumberFormatException ex) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText("Введите число, например 25");
            alert.showAndWait();
        }
    }

    @Override
    public void start(Stage stage) {
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(16));
        grid.setAlignment(Pos.CENTER);

        grid.add(new Label("Температура (°C):"), 0, 0);
        celsiusField = new TextField();
        celsiusField.setPromptText("25");
        celsiusField.setPrefColumnCount(8);
        grid.add(celsiusField, 1, 0);

        resultLabel = new Label("—");
        grid.add(resultLabel, 0, 1, 2, 1);

        Button convertBtn = new Button("Перевести");
        convertBtn.setOnAction(e -> convert());
        Button exitBtn = new Button("Выход");
        exitBtn.setOnAction(e -> stage.close());

        HBox buttons = new HBox(8, convertBtn, exitBtn);
        buttons.setAlignment(Pos.CENTER);
        grid.add(buttons, 0, 2, 2, 1);

        celsiusField.setOnKeyPressed(e -> {
            if (e.getCode() == KeyCode.ENTER) {
                convert();
            }
        });

        Scene scene = new Scene(grid, 340, 160);
        stage.setTitle("Конвертер температуры");
        stage.setResizable(false);
        stage.setScene(scene);
        stage.show();
        celsiusField.requestFocus();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
