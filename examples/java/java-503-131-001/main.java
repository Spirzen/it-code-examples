
import java.util.Random;

public class PasswordGenerator {
    public static void main(String[] args) {
        int length = 12;
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
        
        StringBuilder password = new StringBuilder();
        Random random = new Random();

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(chars.length());
            char ch = chars.charAt(index);
            password.append(ch);
        }

        System.out.println("Сгенерированный пароль: " + password.toString());
    }
}
