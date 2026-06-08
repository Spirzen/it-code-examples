
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class HelloFx extends Application {

    @Override
    public void start(Stage stage) {
        Label prompt = new Label("Введите имя:");
        TextField nameField = new TextField();
        Label greeting = new Label();
        Button greetButton = new Button("Приветствовать");

        greetButton.setOnAction(e -> {
            String name = nameField.getText().trim();
            greeting.setText(name.isEmpty() ? "Введите имя" : "Привет, " + name + "!");
        });

        VBox root = new VBox(10, prompt, nameField, greetButton, greeting);
        root.setStyle("-fx-padding: 20;");

        Scene scene = new Scene(root, 360, 200);
        stage.setTitle("Пример GUI");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
