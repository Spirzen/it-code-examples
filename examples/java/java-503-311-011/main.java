
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class TableDemo {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            String[] columns = {"Имя", "Возраст"};
            Object[][] data = {{"Алиса", 30}, {"Боб", 25}};
            JTable table = new JTable(new DefaultTableModel(data, columns));

            JFrame frame = new JFrame("Таблица");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.add(new JScrollPane(table));
            frame.setSize(400, 200);
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}
