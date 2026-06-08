import javax.swing.*;
import java.awt.*;

public class TempConverter {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Конвертер температуры");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setResizable(false);
            frame.setLocationRelativeTo(null);

            JPanel panel = new JPanel(new GridLayout(3, 2, 8, 8));
            panel.setBorder(BorderFactory.createEmptyBorder(16, 16, 16, 16));

            panel.add(new JLabel("Температура (°C):"));
            JTextField celsiusField = new JTextField(8);
            panel.add(celsiusField);

            JLabel resultLabel = new JLabel("—");
            panel.add(resultLabel);

            JButton convertBtn = new JButton("Перевести");
            panel.add(convertBtn);

            Runnable convert = () -> {
                String raw = celsiusField.getTexttrimreplace(',', '.');
                try {
                    double celsius = Double.parseDouble(raw);
                    double fahrenheit = celsius * 9 / 5 + 32;
                    resultLabel.setText(String.format("%.1f °C = %.1f °F", celsius, fahrenheit));
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Введите число, например 25", "Ошибка", JOptionPane.ERROR_MESSAGE);
                }
            };

            convertBtn.addActionListener(e -> convert.run());
            celsiusField.addActionListener(e -> convert.run());

            frame.add(panel);
            frame.pack();
            frame.setVisible(true);
        });
    }
}
