import javafx.scene.control.TableView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.collections.FXCollections;

public class Person {
    private final String name;
    private final int age;
    public Person(String name, int age) { this.name = name; this.age = age; }
    public String getName() { return name; }
    public int getAge() { return age; }
}

TableView<Person> table = new TableView<>();
TableColumn<Person, String> colName = new TableColumn<>("Имя");
colName.setCellValueFactory(new PropertyValueFactory<>("name"));
TableColumn<Person, Number> colAge = new TableColumn<>("Возраст");
colAge.setCellValueFactory(new PropertyValueFactory<>("age"));
table.getColumns().addAll(colName, colAge);
table.setItems(FXCollections.observableArrayList(new Person("Алиса", 30)));
VBox.setVgrow(table, Priority.ALWAYS);
