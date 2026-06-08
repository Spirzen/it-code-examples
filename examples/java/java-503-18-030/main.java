package com.test;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SpaceInvaders extends JPanel implements ActionListener, KeyListener {
    private static final int BOARD_WIDTH = 800;
    private static final int BOARD_HEIGHT = 600;
    private static final int PLAYER_WIDTH = 40;
    private static final int PLAYER_HEIGHT = 20;
    private static final int ENEMY_ROWS = 5;
    private static final int ENEMY_COLS = 10;
    private static final int ENEMY_WIDTH = 30;
    private static final int ENEMY_HEIGHT = 20;
    private static final int BULLET_SIZE = 4;

    private Timer timer;
    private Player player;
    private List<Enemy> enemies;
    private List<Bullet> bullets;
    private boolean[] keys = new boolean[256];
    private int score = 0;
    private int lives = 3;
    private boolean gameOver = false;
    private boolean gameWon = false;
    private int enemyDirection = 1; // 1 — right, -1 — left
    private int enemyStepDown = 0;

    public SpaceInvaders() {
        setPreferredSize(new Dimension(BOARD_WIDTH, BOARD_HEIGHT));
        setBackground(Color.BLACK);
        setFocusable(true);
        addKeyListener(this);

        initGame();
        timer = new Timer(20, this); // ~50 FPS
        timer.start();
    }

    private void initGame() {
        player = new Player(BOARD_WIDTH / 2 - PLAYER_WIDTH / 2, BOARD_HEIGHT - 40);
        enemies = new ArrayList<>();
        bullets = new ArrayList<>();

        for (int row = 0; row < ENEMY_ROWS; row++) {
            for (int col = 0; col < ENEMY_COLS; col++) {
                int x = 100 + col * (ENEMY_WIDTH + 10);
                int y = 50 + row * (ENEMY_HEIGHT + 10);
                enemies.add(new Enemy(x, y));
            }
        }

        score = 0;
        lives = 3;
        gameOver = false;
        gameWon = false;
        enemyDirection = 1;
        enemyStepDown = 0;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (gameOver) {
            drawGameOver(g);
        } else if (gameWon) {
            drawGameWon(g);
        } else {
            drawPlayer(g);
            drawEnemies(g);
            drawBullets(g);
            drawHUD(g);
        }
    }

    private void drawPlayer(Graphics g) {
        g.setColor(Color.GREEN);
        g.fillRect(player.x, player.y, PLAYER_WIDTH, PLAYER_HEIGHT);
    }

    private void drawEnemies(Graphics g) {
        g.setColor(Color.RED);
        for (Enemy e : enemies) {
            g.fillRect(e.x, e.y, ENEMY_WIDTH, ENEMY_HEIGHT);
        }
    }

    private void drawBullets(Graphics g) {
        g.setColor(Color.WHITE);
        for (Bullet b : bullets) {
            g.fillRect(b.x, b.y, BULLET_SIZE, BULLET_SIZE);
        }
    }

    private void drawHUD(Graphics g) {
        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.PLAIN, 16));
        g.drawString("Score: " + score, 10, 20);
        g.drawString("Lives: " + lives, BOARD_WIDTH - 100, 20);
    }

    private void drawGameOver(Graphics g) {
        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.BOLD, 40));
        FontMetrics fm = g.getFontMetrics();
        String text = "GAME OVER";
        int x = (BOARD_WIDTH - fm.stringWidth(text)) / 2;
        int y = BOARD_HEIGHT / 2;
        g.drawString(text, x, y);
        g.setFont(new Font("Arial", Font.PLAIN, 20));
        g.drawString("Press R to restart", x + 80, y + 40);
    }

    private void drawGameWon(Graphics g) {
        g.setColor(Color.CYAN);
        g.setFont(new Font("Arial", Font.BOLD, 40));
        FontMetrics fm = g.getFontMetrics();
        String text = "YOU WIN!";
        int x = (BOARD_WIDTH - fm.stringWidth(text)) / 2;
        int y = BOARD_HEIGHT / 2;
        g.drawString(text, x, y);
        g.setFont(new Font("Arial", Font.PLAIN, 20));
        g.drawString("Press R to restart", x + 70, y + 40);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (!gameOver && !gameWon) {
            updatePlayer();
            updateBullets();
            updateEnemies();
            checkCollisions();
            checkWinOrLose();
        }
        repaint();
    }

    private void updatePlayer() {
        if (keys[KeyEvent.VK_LEFT] && player.x > 0) {
            player.x -= 5;
        }
        if (keys[KeyEvent.VK_RIGHT] && player.x < BOARD_WIDTH - PLAYER_WIDTH) {
            player.x += 5;
        }
        if (keys[KeyEvent.VK_SPACE]) {
            shoot();
            keys[KeyEvent.VK_SPACE] = false;
        }
    }

    private void shoot() {
        bullets.add(new Bullet(player.x + PLAYER_WIDTH / 2 - BULLET_SIZE / 2, player.y));
    }

    private void updateBullets() {
        bullets.removeIf(b -> b.y < 0);
        for (Bullet b : bullets) {
            b.y -= 7;
        }
    }

    private void updateEnemies() {
        boolean moveDown = false;
        for (Enemy e : enemies) {
            if ((enemyDirection == 1 && e.x + ENEMY_WIDTH >= BOARD_WIDTH - 10) ||
                    (enemyDirection == -1 && e.x <= 10)) {
                moveDown = true;
                break;
            }
        }

        if (moveDown) {
            enemyDirection *= -1;
            for (Enemy e : enemies) {
                e.y += 20;
            }
        } else {
            for (Enemy e : enemies) {
                e.x += 2 * enemyDirection;
            }
        }
    }

    private void checkCollisions() {
        List<Bullet> bulletsToRemove = new ArrayList<>();
        List<Enemy> enemiesToRemove = new ArrayList<>();

        for (Bullet b : bullets) {
            for (Enemy e : enemies) {
                if (b.x < e.x + ENEMY_WIDTH &&
                        b.x + BULLET_SIZE > e.x &&
                        b.y < e.y + ENEMY_HEIGHT &&
                        b.y + BULLET_SIZE > e.y) {
                    bulletsToRemove.add(b);
                    enemiesToRemove.add(e);
                    score += 10;
                    break;
                }
            }
        }

        bullets.removeAll(bulletsToRemove);
        enemies.removeAll(enemiesToRemove);

        for (Enemy e : enemies) {
            if (e.y + ENEMY_HEIGHT >= player.y) {
                lives = 0;
                break;
            }
        }
    }

    private void checkWinOrLose() {
        if (enemies.isEmpty()) {
            gameWon = true;
        }
        if (lives <= 0) {
            gameOver = true;
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        keys[e.getKeyCode()] = true;
        if (e.getKeyCode() == KeyEvent.VK_R && (gameOver || gameWon)) {
            initGame();
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        if (e.getKeyCode() != KeyEvent.VK_SPACE) {
            keys[e.getKeyCode()] = false;
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {}

    private static class Player {
        int x, y;
        Player(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Enemy {
        int x, y;
        Enemy(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Bullet {
        int x, y;
        Bullet(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Space Invaders");
        SpaceInvaders game = new SpaceInvaders();
        frame.add(game);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
