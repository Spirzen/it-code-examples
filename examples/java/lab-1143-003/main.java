import javax.swing.*;

public class HelloButton {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Кнопка");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(280, 140);
            frame.setLocationRelativeTo(null);

            JButton btn = new JButton("Нажми меня");
            btn.addActionListener(e ->
                JOptionPane.showMessageDialog(
                    frame,
                    "Кнопка нажата!",
                    "Сообщение",
                    JOptionPane.INFORMATION_MESSAGE
                )
            );
            frame.add(btn);

            frame.setVisible(true);
        });
    }
}
