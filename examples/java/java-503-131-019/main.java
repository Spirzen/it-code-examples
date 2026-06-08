
import javax.swing.*;
import java.awt.*;

public class LoginForm {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Вход");
            frame.setSize(400, 200);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JPanel panel = new JPanel(new GridLayout(3, 2, 8, 8));
            JTextField nameField = new JTextField();
            JPasswordField passwordField = new JPasswordField();
            JLabel resultLabel = new JLabel(" ");
            JButton submit = new JButton("Отправить");

            submit.addActionListener(e -> {
                String name = nameField.getText().trim();
                char[] password = passwordField.getPassword();
                if (name.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Введите имя", "Ошибка", JOptionPane.ERROR_MESSAGE);
                } else if (password.length < 3) {
                    JOptionPane.showMessageDialog(frame, "Пароль слишком короткий", "Ошибка", JOptionPane.ERROR_MESSAGE);
                } else {
                    resultLabel.setText("Привет, " + name + "!");
                    nameField.setText("");
                    passwordField.setText("");
                }
            });

            panel.add(new JLabel("Имя:"));
            panel.add(nameField);
            panel.add(new JLabel("Пароль:"));
            panel.add(passwordField);
            panel.add(submit);
            panel.add(resultLabel);
            frame.add(panel);
            frame.setVisible(true);
        });
    }
}
