import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

GameState gameState = GameState.MENU;

private void setMoveKey(int code, boolean down) {
    switch (code) {
        case KeyEvent.VK_W, KeyEvent.VK_UP -> up = down;
        case KeyEvent.VK_S, KeyEvent.VK_DOWN -> down = down;
        case KeyEvent.VK_A, KeyEvent.VK_LEFT -> left = down;
        case KeyEvent.VK_D, KeyEvent.VK_RIGHT -> right = down;
        default -> { }
    }
}

GamePanel() {
    // ... после setFocusable(true):
    addKeyListener(new KeyAdapter() {
        @Override
        public void keyPressed(KeyEvent e) {
            setMoveKey(e.getKeyCode(), true);
            if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
                running = false;
                loop.interrupt();
                System.exit(0);
            }
            if (gameState == GameState.MENU && e.getKeyCode() == KeyEvent.VK_ENTER) {
                gameState = GameState.PLAYING;
            }
            if (gameState == GameState.GAME_OVER && e.getKeyCode() == KeyEvent.VK_R) {
                resetRun();
            }
        }

        @Override
        public void keyReleased(KeyEvent e) {
            setMoveKey(e.getKeyCode(), false);
        }
    });
    requestFocusInWindow();
    loop.start();
}

private void update(double dt) {
    if (gameState != GameState.PLAYING) {
        return;
    }
}
