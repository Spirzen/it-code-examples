import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class App extends Application {
    @Override
    public void start(Stage stage) {
        VBox root = new VBox(8);
        stage.setTitle("Моё приложение");
        stage.setScene(new Scene(root, 640, 480));
        stage.setMinWidth(400);
        stage.show();
    }
    public static void main(String[] args) { launch(args); }
}
