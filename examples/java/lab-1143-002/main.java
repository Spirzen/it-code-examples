import javax.swing.*;

public class HelloLabel {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Привет, Swing");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(320, 160);
            frame.setLocationRelativeTo(null);

            JLabel label = new JLabel("Окно работает!", SwingConstants.CENTER);
            frame.add(label);

            frame.setVisible(true);
        });
    }
}
