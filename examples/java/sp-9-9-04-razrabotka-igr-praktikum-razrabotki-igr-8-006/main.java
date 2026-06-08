final Player player = new Player();
boolean up, down, left, right;

// keyPressed / keyReleased — выставляйте флаги для WASD и стрелок

private void update(double dt) {
    if (gameState != GameState.PLAYING) return;
    player.updateMovement(dt, up, down, left, right, WIDTH, HEIGHT, 1.0);
}

@Override
protected void paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2 = (Graphics2D) g;
    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2.setColor(new Color(17, 17, 20));
    g2.fillRect(0, 0, WIDTH, HEIGHT);
    if (gameState == GameState.PLAYING) {
        g2.setColor(new Color(90, 160, 255));
        g2.fill(new java.awt.geom.Ellipse2D.Double(
                player.x - player.radius, player.y - player.radius,
                player.radius * 2, player.radius * 2));
    } else if (gameState == GameState.MENU) {
        g2.drawString("Enter — старт", 400, HEIGHT / 2);
    }
}
