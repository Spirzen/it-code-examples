
import javax.swing.*;

public class SimpleWindow {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Моё первое окно");
            frame.setSize(400, 300);
            frame.setLocationRelativeTo(null);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.add(new JLabel("Привет, Swing!", SwingConstants.CENTER));
            frame.setVisible(true);
        });
    }
}
