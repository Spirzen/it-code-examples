package com.survivors;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.*;

public final class SurvivorsGame {
    private static final int WIDTH = 960;
    private static final int HEIGHT = 540;

    public SurvivorsGame() {
        JFrame frame = new JFrame("Java Survivors — этап 0");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.setContentPane(new GamePanel());
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    static final class GamePanel extends JPanel implements Runnable {
        private volatile boolean running = true;
        private final Thread loop = new Thread(this, "game-loop");

        GamePanel() {
            setPreferredSize(new Dimension(WIDTH, HEIGHT));
            setBackground(new Color(17, 17, 20));
            setFocusable(true);
            loop.start();
        }

        @Override
        public void run() {
            long prev = System.nanoTime();
            while (running) {
                long now = System.nanoTime();
                double dt = (now - prev) / 1_000_000_000.0;
                prev = now;
                dt = Math.min(dt, 0.033);

                update(dt);
                repaint();

                try {
                    Thread.sleep(8);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    running = false;
                }
            }
        }

        private void update(double dt) {
            // пока пусто
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.setColor(new Color(28, 28, 36));
            g.fillRect(0, 0, getWidth(), getHeight());
            g.setColor(new Color(200, 200, 210));
            g.drawString("Этап 0 — игровой цикл работает", 24, 32);
        }
    }
}
