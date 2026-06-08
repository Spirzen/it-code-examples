import javax.swing.*;
import java.awt.*;

public class MenuDemo {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Меню");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 240);
            frame.setLocationRelativeTo(null);

            JMenuBar menuBar = new JMenuBar();
            JMenu fileMenu = new JMenu("Файл");
            JMenuItem newItem = new JMenuItem("Новый");
            JMenuItem exitItem = new JMenuItem("Выход");
            newItem.addActionListener(e -> JOptionPane.showMessageDialog(frame, "Новый"));
            exitItem.addActionListener(e -> frame.dispose());
            fileMenu.add(newItem);
            fileMenu.addSeparator();
            fileMenu.add(exitItem);
            menuBar.add(fileMenu);

            JMenu helpMenu = new JMenu("Справка");
            JMenuItem aboutItem = new JMenuItem("О программе");
            aboutItem.addActionListener(e ->
                JOptionPane.showMessageDialog(frame, "Демо Swing", "О программе", JOptionPane.INFORMATION_MESSAGE)
            );
            helpMenu.add(aboutItem);
            menuBar.add(helpMenu);
            frame.setJMenuBar(menuBar);

            JLabel status = new JLabel(" Готово");
            status.setBorder(BorderFactory.createLoweredBevelBorder());

            frame.add(new JLabel("Рабочая область", SwingConstants.CENTER), BorderLayout.CENTER);
            frame.add(status, BorderLayout.SOUTH);

            frame.setVisible(true);
        });
    }
}
