package apitester.ui

import apitester.jmeter.JMeterHttpExecutor
import apitester.model.HttpRequestConfig
import apitester.model.HttpResponseResult
import groovy.swing.SwingBuilder

import javax.swing.*
import java.awt.*
import java.awt.event.KeyEvent

class ApiTesterFrame extends JFrame {

    private final JMeterHttpExecutor executor = new JMeterHttpExecutor()

    private JTextField urlField
    private JComboBox<String> methodCombo
    private JTextArea headersArea
    private JTextArea bodyArea
    private JTextArea responseBodyArea
    private JTextArea responseHeadersArea
    private JLabel statusLabel
    private JLabel metaLabel
    private JButton sendButton
    private JProgressBar progressBar

    ApiTesterFrame() {
        title = 'Groovy API Tester (JMeter)'
        defaultCloseOperation = EXIT_ON_CLOSE
        minimumSize = new Dimension(900, 650)
        setSize(1000, 720)
        setLocationRelativeTo(null)
        contentPane = buildContent()
        setupShortcuts()
    }
