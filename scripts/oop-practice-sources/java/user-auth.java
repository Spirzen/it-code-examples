class User {
    private String username;
    private String password;
    private boolean loggedIn;

    User(String username, String password) {
        this.username = username;
        this.password = password;
        this.loggedIn = false;
    }

    void login(String password) {
        if (password.equals(this.password)) {
            loggedIn = true;
            System.out.println("Добро пожаловать, " + username + "!");
        } else {
            System.out.println("Ошибка: неверный пароль");
        }
    }

    void logout() {
        loggedIn = false;
        System.out.println(username + " вышел из системы");
    }

    void postMessage(String text) {
        if (!loggedIn) {
            System.out.println("Сначала войдите в систему");
            return;
        }
        System.out.println("Сообщение опубликовано: " + text);
    }
}

public class Main {
    public static void main(String[] args) {
        User user = new User("alex", "secret123");
        user.postMessage("Привет!");
        user.login("wrong");
        user.login("secret123");
        user.postMessage("Привет, мир!");
        user.logout();
        user.postMessage("Ещё одно сообщение");
    }
}
