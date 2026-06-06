import java.util.List;

public class Main {
    record User(int id, String name) {}

    public static void main(String[] args) {
        List<User> users = List.of(new User(1, "Алиса"), new User(2, "Боб"));
        users.forEach(u -> System.out.println(u.id() + ": " + u.name()));
    }
}
