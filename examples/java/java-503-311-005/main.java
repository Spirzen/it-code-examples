
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

public class LabelDemo extends Application {

    @Override
    public void start(Stage stage) {
        Label title = new Label("Заголовок окна");
        title.setFont(Font.font("Arial", FontWeight.BOLD, 18));
        title.setStyle("-fx-text-fill: white; -fx-background-color: black; -fx-padding: 12;");

        Label info = new Label("Это информационная метка.\nТекст может быть многострочным.");
        info.setWrapText(true);
        info.setMaxWidth(280);
        info.setAlignment(Pos.CENTER_LEFT);

        VBox root = new VBox(16, title, info);
        root.setStyle("-fx-padding: 20;");

        stage.setScene(new Scene(root, 360, 220));
        stage.setTitle("Label");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
