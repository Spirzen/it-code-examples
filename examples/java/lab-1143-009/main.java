import javax.swing.*;
import java.awt.*;

public class LoginGrid {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Форма входа");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLocationRelativeTo(null);

            JPanel panel = new JPanel(new GridLayout(3, 2, 8, 8));
            panel.setBorder(BorderFactory.createEmptyBorder(12, 12, 12, 12));

            panel.add(new JLabel("Email:"));
            JTextField email = new JTextField();
            panel.add(email);

            panel.add(new JLabel("Пароль:"));
            JPasswordField password = new JPasswordField();
            panel.add(password);

            panel.add(new JLabel());
            JButton login = new JButton("Войти");
            panel.add(login);

            login.addActionListener(e ->
                JOptionPane.showMessageDialog(frame, "Вход (демо)", "Файл", JOptionPane.INFORMATION_MESSAGE)
            );

            frame.add(panel);
            frame.pack();
            frame.setVisible(true);
        });
    }
}
