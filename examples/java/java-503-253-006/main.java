package com.xmlvalidator.ui;

import com.xmlvalidator.model.ValidationResult;
import com.xmlvalidator.service.XsdValidatorService;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.SwingUtilities;
import javax.swing.SwingWorker;
import javax.swing.UIManager;
import javax.swing.WindowConstants;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.KeyEvent;
import java.nio.file.Path;

public final class XmlValidatorFrame extends JFrame {

    private final XsdValidatorService validatorService = new XsdValidatorService();
    private final FilePanel xmlPanel = new FilePanel("XML-документ", "xml", "Выберите XML-файл");
    private final FilePanel xsdPanel = new FilePanel("XSD-схема", "xsd", "Выберите XSD-файл");
    private final ResultPanel resultPanel = new ResultPanel();
    private final JButton validateButton = new JButton("Проверить");
    private final JButton clearButton = new JButton("Очистить");

    public XmlValidatorFrame() {
        super("XML Validator — проверка по XSD");
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setMinimumSize(new Dimension(960, 640));
        setLocationRelativeTo(null);

        JPanel content = new JPanel(new BorderLayout(12, 12));
        content.setBorder(BorderFactory.createEmptyBorder(12, 12, 12, 12));

        JPanel editors = new JPanel(new GridLayout(1, 2, 12, 0));
        editors.add(xmlPanel);
        editors.add(xsdPanel);

        JSplitPane splitPane = new JSplitPane(JSplitPane.VERTICAL_SPLIT, editors, resultPanel);
        splitPane.setResizeWeight(0.72);
        splitPane.setContinuousLayout(true);
        content.add(splitPane, BorderLayout.CENTER);

        JPanel actions = new JPanel(new FlowLayout(FlowLayout.RIGHT, 8, 0));
        validateButton.setMnemonic(KeyEvent.VK_V);
        clearButton.setMnemonic(KeyEvent.VK_C);
        actions.add(clearButton);
        actions.add(validateButton);
        content.add(actions, BorderLayout.SOUTH);

        setContentPane(content);

        validateButton.addActionListener(e -> runValidation());
        clearButton.addActionListener(e -> clearAll());

        getRootPane().setDefaultButton(validateButton);
    }

    private void clearAll() {
        xmlPanel.clear();
        xsdPanel.clear();
        resultPanel.reset();
    }

    private void runValidation() {
        validateButton.setEnabled(false);
        clearButton.setEnabled(false);
        resultPanel.showPending();

        SwingWorker<ValidationResult, Void> worker = new SwingWorker<>() {
            @Override
            protected ValidationResult doInBackground() {
                Path xmlPath = xmlPanel.getSelectedPath();
                Path xsdPath = xsdPanel.getSelectedPath();
                String xmlText = xmlPanel.getText();
                String xsdText = xsdPanel.getText();

                boolean hasXmlFile = xmlPath != null && !xmlText.isBlank();
                boolean hasXsdFile = xsdPath != null && !xsdText.isBlank();

                if (hasXmlFile && hasXsdFile
                        && xmlText.equals(readQuietly(xmlPath))
                        && xsdText.equals(readQuietly(xsdPath))) {
                    return validatorService.validate(xmlPath, xsdPath);
                }
                return validatorService.validate(xmlText, xsdText);
            }

            @Override
            protected void done() {
                try {
                    resultPanel.showResult(get());
                } catch (Exception ex) {
                    resultPanel.showError(ex.getMessage() != null
                            ? ex.getMessage()
                            : "Неизвестная ошибка при валидации.");
                } finally {
                    validateButton.setEnabled(true);
                    clearButton.setEnabled(true);
                }
            }
        };
        worker.execute();
    }

    private static String readQuietly(Path path) {
        try {
            return java.nio.file.Files.readString(path);
        } catch (Exception ignored) {
            return "";
        }
    }

    public static void launch() {
        applyLookAndFeel();
        SwingUtilities.invokeLater(() -> {
            XmlValidatorFrame frame = new XmlValidatorFrame();
            frame.setVisible(true);
        });
    }

    private static void applyLookAndFeel() {
        try {
            for (UIManager.LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    return;
                }
            }
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {
            // оставляем L&F по умолчанию
        }
    }
}
