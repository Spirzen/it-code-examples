final List<Projectile> projectiles = new ArrayList<>();

// в update после врагов:
player.shotCooldown -= dt;
if (player.shotCooldown <= 0 && !enemies.isEmpty()) {
    shootMagicBolt();
    player.shotCooldown = 0.35;
}

private void shootMagicBolt() {
    Enemy target = findNearestEnemy();
    if (target == null) return;
    double dx = target.x - player.x;
    double dy = target.y - player.y;
    double len = Math.hypot(dx, dy);
    if (len < 0.001) return;
    double speed = 480;
    projectiles.add(new Projectile(
            player.x, player.y,
            (dx / len) * speed, (dy / len) * speed,
            18, 6));
}

private Enemy findNearestEnemy() {
    Enemy best = null;
    double bestD = Double.MAX_VALUE;
    for (Enemy e : enemies) {
        double d = distSq(player.x, player.y, e.x, e.y);
        if (d < bestD) { bestD = d; best = e; }
    }
    return best;
}

static double distSq(double x1, double y1, double x2, double y2) {
    double dx = x1 - x2, dy = y1 - y2;
    return dx * dx + dy * dy;
}
