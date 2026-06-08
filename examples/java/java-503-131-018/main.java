
import javax.swing.*;
import java.awt.*;

public class CounterApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Счётчик");
            frame.setSize(350, 150);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JPanel panel = new JPanel(new FlowLayout());
            JLabel label = new JLabel("Счётчик: 0");
            JButton button = new JButton("Нажми меня");

            int[] counter = {0};
            button.addActionListener(e -> {
                counter[0]++;
                label.setText("Счётчик: " + counter[0]);
            });

            panel.add(button);
            panel.add(label);
            frame.add(panel);
            frame.setVisible(true);
        });
    }
}
