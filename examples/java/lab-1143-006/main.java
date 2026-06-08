import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class SettingsPanel {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Настройки");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLocationRelativeTo(null);

            JPanel panel = new JPanel();
            panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
            panel.setBorder(BorderFactory.createEmptyBorder(16, 16, 16, 16));

            JCheckBox notifyChk = new JCheckBox("Уведомления", true);
            JCheckBox soundChk = new JCheckBox("Звук", false);
            JRadioButton userRole = new JRadioButton("Пользователь", true);
            JRadioButton adminRole = new JRadioButton("Администратор");
            ButtonGroup roleGroup = new ButtonGroup();
            roleGroup.add(userRole);
            roleGroup.add(adminRole);

            JLabel statusLabel = new JLabel();
            statusLabel.setForeground(Color.GRAY);

            Runnable updateStatus = () -> {
                List<String> parts = new ArrayList<>();
                if (notifyChk.isSelected()) parts.add("уведомления");
                if (soundChk.isSelected()) parts.add("звук");
                String role = userRole.isSelected() ? "user" : "admin";
                statusLabel.setText("Роль: " + role + "; включено: " + (parts.isEmpty() ? "ничего" : String.join(", ", parts)));
            };

            notifyChk.addActionListener(e -> updateStatus.run());
            soundChk.addActionListener(e -> updateStatus.run());
            userRole.addActionListener(e -> updateStatus.run());
            adminRole.addActionListener(e -> updateStatus.run());

            panel.add(notifyChk);
            panel.add(soundChk);
            panel.add(Box.createVerticalStrut(12));
            panel.add(new JLabel("Роль:"));
            panel.add(userRole);
            panel.add(adminRole);
            panel.add(Box.createVerticalStrut(12));
            panel.add(statusLabel);

            updateStatus.run();

            frame.add(panel);
            frame.pack();
            frame.setVisible(true);
        });
    }
}
