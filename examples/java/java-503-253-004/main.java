package com.xmlvalidator.ui;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import java.nio.file.Path;

final class FilePanel extends JPanel {

    private final JTextField pathField = new JTextField();
    private final JTextArea textArea = new JTextArea();
    private final JButton browseButton = new JButton("Обзор…");
    private final String extension;
    private final String dialogTitle;
    private Path selectedPath;

    FilePanel(String title, String extension, String dialogTitle) {
        this.extension = extension;
        this.dialogTitle = dialogTitle;

        setLayout(new BorderLayout(8, 8));
        setBorder(BorderFactory.createTitledBorder(title));

        pathField.setEditable(false);
        pathField.setPreferredSize(new Dimension(200, 28));

        JPanel top = new JPanel(new BorderLayout(6, 0));
        top.add(pathField, BorderLayout.CENTER);
        top.add(browseButton, BorderLayout.EAST);
        add(top, BorderLayout.NORTH);

        textArea.setFont(new Font(Font.MONOSPACED, Font.PLAIN, 13));
        textArea.setTabSize(2);
        textArea.setLineWrap(false);
        textArea.setWrapStyleWord(false);

        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setPreferredSize(new Dimension(400, 220));
        add(scrollPane, BorderLayout.CENTER);

        JPanel footer = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
        footer.add(new JLabel("Можно вставить текст или выбрать файл."));
        add(footer, BorderLayout.SOUTH);

        browseButton.addActionListener(e -> chooseFile());
    }

    private void chooseFile() {
        var chooser = new javax.swing.JFileChooser();
        chooser.setDialogTitle(dialogTitle);
        chooser.setFileFilter(new FileNameExtensionFilter(
                extension.toUpperCase() + " (*." + extension + ")", extension));
        if (chooser.showOpenDialog(this) == javax.swing.JFileChooser.APPROVE_OPTION) {
            selectedPath = chooser.getSelectedFile().toPath();
            pathField.setText(selectedPath.toString());
            try {
                textArea.setText(java.nio.file.Files.readString(selectedPath));
                textArea.setCaretPosition(0);
            } catch (Exception ex) {
                javax.swing.JOptionPane.showMessageDialog(
                        this,
                        "Не удалось прочитать файл: " + ex.getMessage(),
                        "Ошибка",
                        javax.swing.JOptionPane.ERROR_MESSAGE
                );
            }
        }
    }

    String getText() {
        return textArea.getText();
    }

    Path getSelectedPath() {
        return selectedPath;
    }

    void clear() {
        selectedPath = null;
        pathField.setText("");
        textArea.setText("");
    }
}
