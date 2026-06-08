
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class ButtonDemo extends Application {

    private void onButtonClick() {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Событие");
        alert.setHeaderText(null);
        alert.setContentText("Кнопка была нажата!");
        alert.showAndWait();
    }

    @Override
    public void start(Stage stage) {
        Button button = new Button("Нажми меня");
        button.setOnAction(e -> onButtonClick());
        button.setMaxWidth(Double.MAX_VALUE);
        button.setStyle("-fx-font-size: 14px; -fx-padding: 10 20;");

        StackPane root = new StackPane(button);
        root.setStyle("-fx-padding: 20;");

        stage.setTitle("Пример кнопки JavaFX");
        stage.setScene(new Scene(root, 320, 180));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
