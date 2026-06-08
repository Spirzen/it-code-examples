if (e.kind == EnemyKind.SHOOTER) {
    double preferred = 180;
    if (len > preferred + 20) {
        e.x += (dx / len) * e.speed * 0.75 * dt;
        e.y += (dy / len) * e.speed * 0.75 * dt;
    } else if (len < preferred - 20) {
        e.x -= (dx / len) * e.speed * 0.75 * dt;
        e.y -= (dy / len) * e.speed * 0.75 * dt;
    }
    if (e.attackCooldown <= 0 && len > 50) {
        projectiles.add(enemyProjectileTowardPlayer(e));
        e.attackCooldown = 1.3;
    }
    continue;
}
