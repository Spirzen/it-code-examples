
package com.example;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.stage.Stage;

public class HelloFx extends Application {

    @Override
    public void start(Stage stage) {
        stage.setTitle("Привет, JavaFX");
        stage.setScene(new Scene(new Label("Окно работает"), 320, 120));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
