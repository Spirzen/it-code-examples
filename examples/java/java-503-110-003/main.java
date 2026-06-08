@Entity
public class User {
    @Id
    private String id;
    private String name;
    private int age;
}

@Inject
private DocumentTemplate template;

// Сохранение
User user = new User("1", "Alice", 30);
template.insert(user);

// Запрос
List<User> adults = template.select(User.class)
    .where("age").gt(18)
    .result();
