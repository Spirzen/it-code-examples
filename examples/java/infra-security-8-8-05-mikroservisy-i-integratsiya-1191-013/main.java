// src/main/java/ru/timur/crm/CrmApplication.java
package ru.timur.crm;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class CrmApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(CrmApplication.class.getResource("/crm-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 1000, 700);
        stage.setTitle("Kafka CRM Demo");
        stage.setScene(scene);

        // Получаем контроллер для корректного завершения
        CrmController controller = fxmlLoader.getController();
        stage.setOnCloseRequest(event -> {
            controller.shutdown();
            System.exit(0);
        });

        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
