import javax.swing.*;

public class AppFrame {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Моё приложение");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 300);
            frame.setLocationRelativeTo(null);

            // --- JLabel, JButton, JPanel — сюда ---

            frame.setVisible(true);
        });
    }
}
