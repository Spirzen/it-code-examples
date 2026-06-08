import javax.swing.*;
import java.awt.*;

public class CounterApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Счётчик");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(320, 120);
            frame.setLocationRelativeTo(null);

            JLabel label = new JLabel("Счётчик: 0", SwingConstants.CENTER);
            JButton button = new JButton("Нажми меня");

            int[] counter = {0};
            button.addActionListener(e -> {
                counter[0]++;
                label.setText("Счётчик: " + counter[0]);
            });

            JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 8, 16));
            panel.add(button);
            panel.add(label);

            frame.add(panel);
            frame.setVisible(true);
        });
    }
}
