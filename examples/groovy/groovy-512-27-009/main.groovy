package apitester

import apitester.ui.ApiTesterFrame
import javax.swing.SwingUtilities
import javax.swing.UIManager

class Main {

    static void main(String[] args) {
        SwingUtilities.invokeLater {
            try {
                UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName())
            } catch (Exception ignored) {
            }
            new ApiTesterFrame().visible = true
        }
    }
}
