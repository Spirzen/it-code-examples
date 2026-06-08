@Override
protected void paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2 = (Graphics2D) g;
    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2.setColor(GameColors.BG);
    g2.fillRect(0, 0, WIDTH, HEIGHT);

    if (gameState == GameState.PLAYING) {
        drawXpOrbs(g2);
        drawEnemies(g2);
        drawProjectiles(g2);
        drawParticles(g2);
        drawPlayer(g2);
        drawDamageNumbers(g2);
        drawHud(g2);
        if (upgradeState == UpgradeState.PAUSED_FOR_UPGRADE) {
            drawUpgradeOverlay(g2);
        }
    } else if (gameState == GameState.MENU) {
        drawMenu(g2);
    } else if (gameState == GameState.GAME_OVER) {
        drawGameOver(g2);
    }
}
