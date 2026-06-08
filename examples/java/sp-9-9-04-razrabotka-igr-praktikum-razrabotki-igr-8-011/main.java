private void updateProjectiles(double dt) {
    Iterator<Projectile> it = projectiles.iterator();
    while (it.hasNext()) {
        Projectile p = it.next();
        p.x += p.vx * dt;
        p.y += p.vy * dt;
        p.life -= dt;
        if (p.life <= 0 || p.x < -80 || p.x > WIDTH + 80 || p.y < -80 || p.y > HEIGHT + 80) {
            it.remove();
        }
    }
}

private void drawProjectiles(Graphics2D g2) {
    g2.setColor(GameColors.PROJECTILE);
    for (Projectile p : projectiles) {
        g2.fill(new java.awt.geom.Ellipse2D.Double(
                p.x - p.radius, p.y - p.radius, p.radius * 2, p.radius * 2));
    }
}
