import javax.swing.*;
import javax.swing.event.ChangeListener;
import java.awt.*;

public class VolumeSlider {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Ползунок");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(360, 140);
            frame.setLocationRelativeTo(null);

            JLabel volumeLabel = new JLabel("Громкость: 50%", SwingConstants.CENTER);
            volumeLabel.setFont(volumeLabel.getFontderiveFont(14f));

            JSlider slider = new JSlider(0, 100, 50);
            slider.setMajorTickSpacing(25);
            slider.setPaintTicks(true);

            ChangeListener onChange = e -> {
                if (!slider.getValueIsAdjusting()) {
                    volumeLabel.setText("Громкость: " + slider.getValue() + "%");
                }
            };
            slider.addChangeListener(onChange);

            JPanel panel = new JPanel(new BorderLayout(8, 8));
            panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
            panel.add(volumeLabel, BorderLayout.NORTH);
            panel.add(slider, BorderLayout.CENTER);

            frame.add(panel);
            frame.setVisible(true);
        });
    }
}
