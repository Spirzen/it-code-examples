import javax.swing.*;
import java.awt.*;

public class HelloForm {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Приветствие");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setResizable(false);
            frame.setLocationRelativeTo(null);

            JPanel panel = new JPanel(new GridLayout(2, 2, 8, 8));
            panel.setBorder(BorderFactory.createEmptyBorder(16, 16, 16, 16));

            panel.add(new JLabel("Ваше имя:"));
            JTextField nameField = new JTextField(16);
            panel.add(nameField);

            JButton greetBtn = new JButton("Приветствовать");
            panel.add(new JLabel());
            panel.add(greetBtn);

            greetBtn.addActionListener(e -> {
                String name = nameField.getTexttrim();
                if (name.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Введите имя", "Пусто", JOptionPane.WARNING_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(frame, "Здравствуй, " + name + "!", "Привет", JOptionPane.INFORMATION_MESSAGE);
                }
            });

            nameField.addActionListener(e -> greetBtn.doClick());

            frame.add(panel);
            frame.pack();
            frame.setVisible(true);
        });
    }
}
