
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;

MenuBar menuBar = new MenuBar();
Menu fileMenu = new Menu("Файл");
MenuItem exitItem = new MenuItem("Выход");
exitItem.setOnAction(e -> stage.close());
fileMenu.getItems().add(exitItem);
menuBar.getMenus().add(fileMenu);

import javafx.scene.layout.BorderPane;

BorderPane root = new BorderPane();
root.setTop(menuBar);
root.setCenter(grid);
stage.setScene(new Scene(root, 340, 200));
