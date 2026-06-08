/**
 * Пользователь системы.
 */
public class User {
    /**
     * @param name имя пользователя
     * @param age возраст в годах
     */
    public User(String name, int age) { /* ... */ }

    /**
     * @return true, если возраст ≥ 18
     */
    public boolean isAdult() { return age >= 18; }
}
