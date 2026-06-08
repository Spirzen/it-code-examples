
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.util.Duration;

public class CountdownApp extends Application {

    private int count = 10;

    @Override
    public void start(Stage stage) {
        Label label = new Label("Осталось: " + count);
        label.setStyle("-fx-font-size: 24px;");

        Timeline timeline = new Timeline();
        timeline.getKeyFrames().add(new KeyFrame(Duration.seconds(1), e -> {
            count--;
            label.setText(count > 0 ? "Осталось: " + count : "Время вышло!");
            if (count <= 0) {
                timeline.stop();
            }
        }));
        timeline.setCycleCount(Timeline.INDEFINITE);
        timeline.play();

        stage.setScene(new Scene(new StackPane(label), 300, 120));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
