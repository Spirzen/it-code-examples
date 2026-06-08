package com.xmlvalidator.ui;

import com.xmlvalidator.model.ValidationResult;

import javax.swing.BorderFactory;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;

final class ResultPanel extends JPanel {

    private static final Color SUCCESS = new Color(34, 120, 70);
    private static final Color FAILURE = new Color(180, 45, 45);
    private static final Color NEUTRAL = new Color(70, 70, 70);

    private final JLabel statusLabel = new JLabel("Готов к проверке");
    private final JTextArea detailsArea = new JTextArea();

    ResultPanel() {
        setLayout(new BorderLayout(8, 8));
        setBorder(BorderFactory.createTitledBorder("Результат"));

        statusLabel.setFont(statusLabel.getFont().deriveFont(Font.BOLD, 14f));
        add(statusLabel, BorderLayout.NORTH);

        detailsArea.setEditable(false);
        detailsArea.setFont(new Font(Font.MONOSPACED, Font.PLAIN, 13));
        detailsArea.setBackground(new Color(250, 250, 250));
        detailsArea.setLineWrap(true);
        detailsArea.setWrapStyleWord(true);

        JScrollPane scrollPane = new JScrollPane(detailsArea);
        scrollPane.setPreferredSize(new Dimension(200, 140));
        add(scrollPane, BorderLayout.CENTER);
    }

    void reset() {
        statusLabel.setText("Готов к проверке");
        statusLabel.setForeground(NEUTRAL);
        detailsArea.setText("");
        detailsArea.setCaretPosition(0);
    }

    void showPending() {
        statusLabel.setText("Проверка…");
        statusLabel.setForeground(NEUTRAL);
        detailsArea.setText("");
    }

    void showResult(ValidationResult result) {
        if (result.isValid()) {
            statusLabel.setText("✓ " + result.getSummary());
            statusLabel.setForeground(SUCCESS);
            detailsArea.setText("Ошибок не обнаружено.");
        } else {
            statusLabel.setText("✗ " + result.getSummary());
            statusLabel.setForeground(FAILURE);
            StringBuilder sb = new StringBuilder();
            int index = 1;
            for (ValidationResult.ValidationError error : result.getErrors()) {
                if (index > 1) {
                    sb.append('\n').append('\n');
                }
                sb.append(index++).append(". ").append(error.formatted());
            }
            detailsArea.setText(sb.toString());
        }
        detailsArea.setCaretPosition(0);
    }

    void showError(String message) {
        statusLabel.setText("✗ Ошибка");
        statusLabel.setForeground(FAILURE);
        detailsArea.setText(message);
        detailsArea.setCaretPosition(0);
    }
}
