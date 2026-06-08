private int score = 0;
final List<XpOrb> xpOrbs = new ArrayList<>();

private void updateProjectiles(double dt) {
    Iterator<Projectile> it = projectiles.iterator();
    while (it.hasNext()) {
        Projectile p = it.next();
        p.x += p.vx * dt;
        p.y += p.vy * dt;
        p.life -= dt;
        if (p.life <= 0 || p.x < -80 || p.x > WIDTH + 80 || p.y < -80 || p.y > HEIGHT + 80) {
            it.remove();
            continue;
        }
        Enemy hit = null;
        for (Enemy e : enemies) {
            if (circlesHit(p.x, p.y, p.radius, e.x, e.y, e.radius)) {
                hit = e;
                break;
            }
        }
        if (hit != null) {
            damageEnemy(hit, p.damage);
            it.remove();
        }
    }
}

private void damageEnemy(Enemy enemy, double damage) {
    enemy.hp -= damage;
    if (enemy.hp <= 0) {
        enemies.remove(enemy);
        score += enemy.xpValue * 3;
        xpOrbs.add(new XpOrb(enemy.x, enemy.y, enemy.xpValue));
    }
}

static boolean circlesHit(double x1, double y1, double r1, double x2, double y2, double r2) {
    double sum = r1 + r2;
    return distSq(x1, y1, x2, y2) <= sum * sum;
}
