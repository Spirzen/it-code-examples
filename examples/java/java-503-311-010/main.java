
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class LoginFormFx extends Application {

    @Override
    public void start(Stage stage) {
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(20));

        TextField nameField = new TextField();
        PasswordField passwordField = new PasswordField();
        Label result = new Label(" ");
        Button submit = new Button("Войти");

        submit.setOnAction(e -> {
            String name = nameField.getText().trim();
            String password = passwordField.getText();
            if (name.isEmpty()) {
                new Alert(Alert.AlertType.ERROR, "Введите имя").showAndWait();
            } else if (password.length() < 3) {
                new Alert(Alert.AlertType.ERROR, "Пароль слишком короткий").showAndWait();
            } else {
                result.setText("Привет, " + name + "!");
                nameField.clear();
                passwordField.clear();
            }
        });

        grid.add(new Label("Имя:"), 0, 0);
        grid.add(nameField, 1, 0);
        grid.add(new Label("Пароль:"), 0, 1);
        grid.add(passwordField, 1, 1);
        grid.add(submit, 1, 2);
        grid.add(result, 1, 3);

        stage.setScene(new Scene(grid, 400, 200));
        stage.setTitle("Вход");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
