package com.test;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import java.util.*;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

public class Match3Game extends JPanel {
    // Размеры игрового поля
    private static final int ROWS = 8;
    private static final int COLS = 8;
    private static final int TILE_SIZE = 70;
    private static final int TYPES_COUNT = 7;

    // Цвета фишек с градиентом
    private static final Color[] COLORS = {
            new Color(255, 100, 100), // Красный
            new Color(100, 150, 255), // Синий
            new Color(100, 255, 100), // Зеленый
            new Color(255, 255, 100), // Желтый
            new Color(255, 150, 100), // Оранжевый
            new Color(200, 100, 255), // Фиолетовый
            new Color(100, 255, 200)  // Бирюзовый
    };

    private int[][] board;
    private int score;
    private int combo;
    private int selectedX = -1, selectedY = -1;
    private boolean isAnimating = false;
    private List<Animation> animations;
    private List<Particle> particles;
    private javax.swing.Timer gameTimer;
    private float timeOfDay = 0;

    // Эффекты
    private static class Animation {
        int x, y;
        float progress;
        int type; // 0 - падение, 1 - исчезновение, 2 - замена
        int startValue, endValue;

        Animation(int x, int y, int type) {
            this.x = x;
            this.y = y;
            this.type = type;
            this.progress = 0;
        }
    }

    private static class Particle {
        float x, y;
        float vx, vy;
        int life;
        Color color;

        Particle(float x, float y, Color color) {
            this.x = x;
            this.y = y;
            this.vx = (float)(Math.random() - 0.5) * 8;
            this.vy = (float)(Math.random() - 0.5) * 8 - 5;
            this.life = 30;
            this.color = color;
        }

        void update() {
            x += vx;
            y += vy;
            vy += 0.3;
            life--;
        }
    }

    public Match3Game() {
        setPreferredSize(new Dimension(COLS * TILE_SIZE, ROWS * TILE_SIZE + 80));
        setBackground(new Color(20, 30, 45));

        board = new int[ROWS][COLS];
        score = 0;
        combo = 0;
        animations = new ArrayList<>();
        particles = new ArrayList<>();

        initBoard();
        removeAllMatches();

        // Обработка мыши с визуальной обратной связью
        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (!isAnimating) {
                    int x = e.getX() / TILE_SIZE;
                    int y = e.getY() / TILE_SIZE;
                    if (x >= 0 && x < COLS && y >= 0 && y < ROWS) {
                        if (selectedX == -1) {
                            selectedX = x;
                            selectedY = y;
                            repaint();
                        } else {
                            trySwap(selectedX, selectedY, x, y);
                            selectedX = -1;
                            selectedY = -1;
                        }
                    } else {
                        selectedX = -1;
                        selectedY = -1;
                        repaint();
                    }
                }
            }
        });

        // Таймер для анимации и эффектов
        gameTimer = new javax.swing.Timer(16, e -> {
            updateAnimations();
            updateParticles();
            timeOfDay += 0.02;
            repaint();
        });
        gameTimer.start();
    }

    private void initBoard() {
        Random rand = new Random();
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                board[i][j] = rand.nextInt(TYPES_COUNT);
            }
        }
    }

    private void removeAllMatches() {
        boolean hasMatches;
        do {
            hasMatches = false;
            for (int i = 0; i < ROWS; i++) {
                for (int j = 0; j < COLS; j++) {
                    if (isMatchAt(i, j)) {
                        board[i][j] = (board[i][j] + 1) % TYPES_COUNT;
                        hasMatches = true;
                    }
                }
            }
        } while (hasMatches);
    }

    private boolean isMatchAt(int row, int col) {
        int value = board[row][col];
        if (value == -1) return false;

        int count = 1;
        for (int j = col - 1; j >= 0 && board[row][j] == value; j--) count++;
        for (int j = col + 1; j < COLS && board[row][j] == value; j++) count++;
        if (count >= 3) return true;

        count = 1;
        for (int i = row - 1; i >= 0 && board[i][col] == value; i--) count++;
        for (int i = row + 1; i < ROWS && board[i][col] == value; i++) count++;
        return count >= 3;
    }

    private List<Point> findAllMatches() {
        List<Point> matches = new ArrayList<>();
        boolean[][] marked = new boolean[ROWS][COLS];

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                int value = board[i][j];
                if (value == -1) continue;

                int hCount = 1;
                for (int k = j + 1; k < COLS && board[i][k] == value; k++) hCount++;
                if (hCount >= 3) {
                    for (int k = 0; k < hCount; k++) {
                        marked[i][j + k] = true;
                    }
                }

                int vCount = 1;
                for (int k = i + 1; k < ROWS && board[k][j] == value; k++) vCount++;
                if (vCount >= 3) {
                    for (int k = 0; k < vCount; k++) {
                        marked[i + k][j] = true;
                    }
                }
            }
        }

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (marked[i][j]) {
                    matches.add(new Point(j, i));
                    // Добавляем частицы для эффекта взрыва
                    addExplosionParticles(j * TILE_SIZE + TILE_SIZE/2, i * TILE_SIZE + TILE_SIZE/2, COLORS[board[i][j]]);
                }
            }
        }

        return matches;
    }

    private void addExplosionParticles(float x, float y, Color color) {
        for (int i = 0; i < 15; i++) {
            particles.add(new Particle(x, y, color));
        }
    }

    private int removeMatches() {
        List<Point> matches = findAllMatches();
        if (matches.isEmpty()) return 0;

        int points = matches.size() * 10;
        combo++;
        points *= (1 + combo / 10);
        score += points;

        // Добавляем эффект комбо
        if (combo > 1) {
            addComboEffect(points);
        }

        for (Point p : matches) {
            board[p.y][p.x] = -1;
            animations.add(new Animation(p.x, p.y, 1));
        }

        return points;
    }

    private void addComboEffect(int points) {
        // Эффект комбо будет отображаться при отрисовке
    }

    private void applyGravity() {
        for (int j = 0; j < COLS; j++) {
            int writeRow = ROWS - 1;
            for (int i = ROWS - 1; i >= 0; i--) {
                if (board[i][j] != -1) {
                    if (writeRow != i) {
                        animations.add(new Animation(j, i, 0));
                    }
                    board[writeRow--][j] = board[i][j];
                }
            }
            for (int i = writeRow; i >= 0; i--) {
                board[i][j] = -1;
            }
        }
    }

    private void refillBoard() {
        Random rand = new Random();
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (board[i][j] == -1) {
                    board[i][j] = rand.nextInt(TYPES_COUNT);
                    animations.add(new Animation(j, i, 2));
                }
            }
        }
    }

    private boolean processMatches() {
        int points = removeMatches();
        if (points > 0) {
            applyGravity();
            refillBoard();
            return true;
        }
        return false;
    }

    private void processAllMatches() {
        isAnimating = true;
        new Thread(() -> {
            while (processMatches()) {
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            isAnimating = false;
            combo = 0;
        }).start();
    }

    private void trySwap(int x1, int y1, int x2, int y2) {
        if (Math.abs(x1 - x2) + Math.abs(y1 - y2) != 1) return;

        int temp = board[y1][x1];
        board[y1][x1] = board[y2][x2];
        board[y2][x2] = temp;

        List<Point> matches = findAllMatches();
        if (!matches.isEmpty()) {
            processAllMatches();
        } else {
            temp = board[y1][x1];
            board[y1][x1] = board[y2][x2];
            board[y2][x2] = temp;
            // Анимация ошибки
            shakeTile(x1, y1);
            shakeTile(x2, y2);
        }

        repaint();
    }

    private void shakeTile(int x, int y) {
        animations.add(new Animation(x, y, 3));
    }

    private void updateAnimations() {
        animations.removeIf(anim -> {
            anim.progress += 0.1;
            return anim.progress >= 1;
        });
    }

    private void updateParticles() {
        particles.removeIf(p -> p.life <= 0);
        particles.forEach(p -> p.update());
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Градиентный фон
        GradientPaint gradient = new GradientPaint(0, 0, new Color(20, 30, 45),
                getWidth(), getHeight(), new Color(35, 45, 65));
        g2d.setPaint(gradient);
        g2d.fillRect(0, 0, getWidth(), getHeight());

        // Рисуем сетку и фишки
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                int x = j * TILE_SIZE;
                int y = i * TILE_SIZE;

                if (board[i][j] != -1) {
                    // Проверяем анимацию для этой позиции
                    boolean isAnimating = false;
                    for (Animation anim : animations) {
                        if (anim.x == j && anim.y == i) {
                            isAnimating = true;
                            break;
                        }
                    }

                    // Рисуем фишку с эффектом
                    drawTile(g2d, x, y, board[i][j], isAnimating);
                } else {
                    // Пустая клетка
                    g2d.setColor(new Color(45, 55, 75));
                    g2d.fillRoundRect(x + 2, y + 2, TILE_SIZE - 4, TILE_SIZE - 4, 10, 10);
                }

                // Рисуем рамку
                g2d.setColor(new Color(100, 120, 150, 100));
                g2d.drawRoundRect(x + 1, y + 1, TILE_SIZE - 2, TILE_SIZE - 2, 12, 12);
            }
        }

        // Рисуем выделение выбранной фишки
        if (selectedX != -1 && selectedY != -1 && !isAnimating) {
            int x = selectedX * TILE_SIZE;
            int y = selectedY * TILE_SIZE;
            g2d.setColor(new Color(255, 255, 100, 150));
            g2d.setStroke(new BasicStroke(3));
            g2d.drawRoundRect(x + 3, y + 3, TILE_SIZE - 6, TILE_SIZE - 6, 12, 12);

            // Пульсирующий эффект
            float pulse = (float)(Math.sin(System.currentTimeMillis() / 100.0) * 0.3 + 0.7);
            g2d.setColor(new Color(255, 255, 200, (int)(50 * pulse)));
            g2d.fillRoundRect(x + 3, y + 3, TILE_SIZE - 6, TILE_SIZE - 6, 12, 12);
        }

        // Рисуем частицы
        for (Particle p : particles) {
            float alpha = p.life / 30f;
            g2d.setColor(new Color(p.color.getRed(), p.color.getGreen(), p.color.getBlue(), (int)(alpha * 255)));
            g2d.fillOval((int)p.x - 3, (int)p.y - 3, 6, 6);
        }

        // Рисуем интерфейс
        drawUI(g2d);
    }

    private void drawTile(Graphics2D g2d, int x, int y, int type, boolean animating) {
        Color baseColor = COLORS[type];
        Color lightColor = baseColor.brighter();
        Color darkColor = baseColor.darker();

        // Градиентная заливка
        GradientPaint gradient = new GradientPaint(x, y, lightColor,
                x + TILE_SIZE, y + TILE_SIZE, darkColor);
        g2d.setPaint(gradient);

        // Анимация для падающих/исчезающих фишек
        if (animating) {
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.7f));
        }

        g2d.fillRoundRect(x + 2, y + 2, TILE_SIZE - 4, TILE_SIZE - 4, 15, 15);

        // Блик
        g2d.setColor(new Color(255, 255, 255, 100));
        g2d.fillRoundRect(x + 4, y + 4, TILE_SIZE - 8, TILE_SIZE / 3, 10, 10);

        // Узор на фишке
        g2d.setColor(new Color(255, 255, 255, 80));
        g2d.setStroke(new BasicStroke(2));
        g2d.drawRoundRect(x + 5, y + 5, TILE_SIZE - 10, TILE_SIZE - 10, 10, 10);

        // Центральная точка
        g2d.fillOval(x + TILE_SIZE/2 - 3, y + TILE_SIZE/2 - 3, 6, 6);

        if (animating) {
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 1.0f));
        }
    }

    private void drawUI(Graphics2D g2d) {
        int uiY = ROWS * TILE_SIZE + 20;

        // Фон для счета
        g2d.setColor(new Color(0, 0, 0, 150));
        g2d.fillRoundRect(10, uiY - 10, 250, 60, 15, 15);

        // Счет
        g2d.setColor(Color.WHITE);
        g2d.setFont(new Font("Arial", Font.BOLD, 28));
        g2d.drawString("Score: " + score, 20, uiY + 25);

        // Комбо
        if (combo > 1) {
            g2d.setFont(new Font("Arial", Font.BOLD, 24));
            g2d.setColor(new Color(255, 200, 0));
            String comboText = "COMBO x" + combo + "!";
            FontMetrics fm = g2d.getFontMetrics();
            int textWidth = fm.stringWidth(comboText);
            g2d.drawString(comboText, getWidth() - textWidth - 20, uiY + 25);
        }

        // Подсказка
        g2d.setFont(new Font("Arial", Font.PLAIN, 14));
        g2d.setColor(new Color(200, 200, 200));
        g2d.drawString("Click on a tile to select, then click on adjacent tile to swap",
                20, uiY + 55);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("✨ Match3 - Три в ряд ✨");
            Match3Game game = new Match3Game();

            frame.add(game);
            frame.pack();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setResizable(false);
            frame.setLocationRelativeTo(null);

            // Красивая иконка (опционально)
            try {
                frame.setIconImage(Toolkit.getDefaultToolkit().getImage(
                        Match3Game.class.getResource("/icon.png")));
            } catch (Exception e) {
                // Игнорируем, если нет иконки
            }

            frame.setVisible(true);
        });
    }
}
