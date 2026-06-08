
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.text.MessageFormat;
import java.util.Locale;
import java.util.ResourceBundle;

public class MainApp extends Application {
    private ResourceBundle resources;

    @Override
    public void init() {
        // Определяем локаль: сначала из системной, можно переопределить через аргументы
        Locale locale = Locale.getDefault();
        resources = ResourceBundle.getBundle("i18n.messages", locale);
    }

    @Override
    public void start(Stage primaryStage) {
        Button greetButton = new Button(resources.getString("button.greet"));
        Label outputLabel = new Label();

        greetButton.setOnAction(e -> {
            String greeting = resources.getString("greeting");
            String formatted = MessageFormat.format(greeting, "Тимур");
            outputLabel.setText(formatted);
        });

        VBox root = new VBox(10, greetButton, outputLabel);
        Scene scene = new Scene(root, 300, 150);
        primaryStage.setTitle(resources.getString("app.title"));
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
