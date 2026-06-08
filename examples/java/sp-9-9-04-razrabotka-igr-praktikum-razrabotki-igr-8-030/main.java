private static Image playerSprite;
private static Image enemySprite;
private static boolean imagesLoaded;

private void loadAssets() {
    if (imagesLoaded) return;
    Toolkit toolkit = Toolkit.getDefaultToolkit();
    try {
        playerSprite = toolkit.getImage("assets/player.png");
        enemySprite = toolkit.getImage("assets/enemy_normal.png");
        MediaTracker tracker = new MediaTracker(new JPanel());
        tracker.addImage(playerSprite, 0);
        tracker.addImage(enemySprite, 1);
        tracker.waitForAll();
        imagesLoaded = true;
    } catch (Exception ex) {
        System.err.println("Ассеты не загружены: " + ex.getMessage());
        imagesLoaded = false;
    }
}

private void drawPlayer(Graphics2D g2) {
    if (imagesLoaded && playerSprite != null) {
        int size = 32;
        g2.drawImage(playerSprite, (int) player.x - size / 2, (int) player.y - size / 2, size, size, this);
    } else {
        g2.setColor(GameColors.PLAYER);
        g2.fill(new java.awt.geom.Ellipse2D.Double(
                player.x - player.radius, player.y - player.radius,
                player.radius * 2, player.radius * 2));
    }
}
