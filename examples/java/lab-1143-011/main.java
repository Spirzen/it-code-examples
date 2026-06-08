import javax.swing.*;
import java.awt.*;

public class MiniCalc {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Калькулятор");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setResizable(false);
            frame.setLocationRelativeTo(null);

            JTextField aField = new JTextField(6);
            JTextField bField = new JTextField(6);
            JLabel result = new JLabel("Результат: —");

            Runnable calc = (String op) -> {
                try {
                    double a = Double.parseDouble(aField.getTexttrimreplace(',', '.'));
                    double b = Double.parseDouble(bField.getTexttrimreplace(',', '.'));
                    double r = "+".equals(op) ? a + b : a - b;
                    result.setText("Результат: " + r);
                } catch (NumberFormatException ex) {
                    result.setText("Результат: ошибка ввода");
                }
            };

            JPanel panel = new JPanel(new GridBagLayout());
            panel.setBorder(BorderFactory.createEmptyBorder(12, 12, 12, 12));
            GridBagConstraints c = new GridBagConstraints();
            c.insets = new Insets(4, 4, 4, 4);
            c.fill = GridBagConstraints.HORIZONTAL;

            c.gridx = 0; c.gridy = 0; panel.add(new JLabel("A:"), c);
            c.gridx = 1; panel.add(aField, c);
            c.gridx = 0; c.gridy = 1; panel.add(new JLabel("B:"), c);
            c.gridx = 1; panel.add(bField, c);

            JPanel ops = new JPanel(new FlowLayout(FlowLayout.LEFT, 4, 0));
            JButton plus = new JButton("+");
            JButton minus = new JButton("−");
            plus.addActionListener(e -> calc.run("+"));
            minus.addActionListener(e -> calc.run("-"));
            ops.add(plus);
            ops.add(minus);

            c.gridx = 0; c.gridy = 2; c.gridwidth = 2;
            panel.add(ops, c);
            c.gridy = 3;
            panel.add(result, c);

            frame.add(panel);
            frame.pack();
            frame.setVisible(true);
        });
    }
}
