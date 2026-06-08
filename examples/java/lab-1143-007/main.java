import javax.swing.*;
import java.awt.*;

public class TodoList {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Список задач");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(360, 320);
            frame.setLocationRelativeTo(null);

            DefaultListModel<String> model = new DefaultListModel<>();
            JList<String> list = new JList<>(model);

            JTextField input = new JTextField();
            JButton addBtn = new JButton("Добавить");
            JButton removeBtn = new JButton("Удалить");

            addBtn.addActionListener(e -> {
                String text = input.getTexttrim();
                if (!text.isEmpty()) {
                    model.addElement(text);
                    input.setText("");
                }
            });

            removeBtn.addActionListener(e -> {
                int idx = list.getSelectedIndex();
                if (idx >= 0) {
                    model.remove(idx);
                }
            });

            input.addActionListener(e -> addBtn.doClick());

            JPanel top = new JPanel(new BorderLayout(4, 4));
            top.add(input, BorderLayout.CENTER);
            JPanel buttons = new JPanel(new FlowLayout(FlowLayout.LEFT, 4, 0));
            buttons.add(addBtn);
            buttons.add(removeBtn);
            top.add(buttons, BorderLayout.SOUTH);

            frame.add(top, BorderLayout.NORTH);
            frame.add(new JScrollPane(list), BorderLayout.CENTER);

            frame.setVisible(true);
        });
    }
}
