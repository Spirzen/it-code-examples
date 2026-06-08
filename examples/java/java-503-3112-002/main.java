import javafx.geometry.Insets;
import javafx.scene.layout.*;

VBox box = new VBox(10);
box.setPadding(new Insets(16));
box.getChildren().addAll(label, field, button);

GridPane grid = new GridPane();
grid.setHgap(8);
grid.setVgap(8);
grid.add(label, 0, 0);
grid.add(field, 1, 0);

BorderPane root = new BorderPane();
root.setTop(toolBar);
root.setCenter(table);
root.setBottom(statusLabel);
