private int wave = 1;
private double waveTimer = 0;

// в update:
waveTimer += dt;
if (waveTimer >= 30) {
    waveTimer = 0;
    wave++;
}

private void drawHud(Graphics2D g2) {
    int barW = 220, barH = 14, x = 16, y = 16;
    g2.setColor(new Color(40, 40, 50));
    g2.fillRect(x, y, barW, barH);
    double hpRatio = player.hp / player.maxHp;
    g2.setColor(new Color(200, 60, 60));
    g2.fillRect(x, y, (int) (barW * hpRatio), barH);

    g2.fillRect(x, y + 24, barW, barH);
    double xpRatio = (double) player.xp / player.xpToNext;
    g2.setColor(new Color(80, 180, 255));
    g2.fillRect(x, y + 24, (int) (barW * xpRatio), barH);

    g2.setColor(Color.WHITE);
    g2.drawString("LV " + player.level + "  SCORE " + score, x, y + 56);
    g2.drawString(String.format("TIME %d:%02d  WAVE %d", (int) worldTime / 60, (int) worldTime % 60, wave), x, y + 72);
}
