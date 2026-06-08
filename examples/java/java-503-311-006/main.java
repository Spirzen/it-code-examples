
import javafx.application.Application;
import javafx.beans.binding.Bindings;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class BindingDemo extends Application {

    @Override
    public void start(Stage stage) {
        TextField field = new TextField();
        field.setPromptText("Введите текст");

        Label mirror = new Label();
        mirror.textProperty().bind(
            Bindings.concat("Вы ввели: ", field.textProperty())
        );

        Button clear = new Button("Очистить");
        clear.setOnAction(e -> field.clear());

        stage.setScene(new Scene(new VBox(10, field, mirror, clear), 360, 160));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
