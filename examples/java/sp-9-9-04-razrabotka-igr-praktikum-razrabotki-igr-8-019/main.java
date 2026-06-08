private double totalDamageMultiplier() {
    return player.damageMultiplier;
}

private void shootMagicBolt() {
    Enemy target = findNearestEnemy();
    if (target == null) return;
    double dx = target.x - player.x;
    double dy = target.y - player.y;
    double baseAngle = Math.atan2(dy, dx);
    spawnProjectileAtAngle(baseAngle, 18.0, 6.0, 480.0, 0);
}

private void shootTripleCast() {
    Enemy target = findNearestEnemy();
    if (target == null) return;
    double baseAngle = Math.atan2(target.y - player.y, target.x - player.x);
    double spread = 0.44;
    for (int i = 0; i < 3; i++) {
        double offset = (i - 1) * (spread / 2);
        spawnProjectileAtAngle(baseAngle + offset, 12.0, 5.5, 540.0, 0);
    }
}

private void shootPulseRing() {
    int count = 10;
    for (int i = 0; i < count; i++) {
        double angle = (Math.PI * 2.0 / count) * i;
        spawnProjectileAtAngle(angle, 14.0, 5.0, 430.0, 0);
    }
}

private void spawnProjectileAtAngle(double angle, double baseDamage, double baseRadius,
                                  double baseSpeed, int pierce) {
    double speed = baseSpeed * player.projectileSpeedMultiplier;
    double damage = baseDamage * totalDamageMultiplier() + player.flatDamageBonus;
    double radius = baseRadius;
    double vx = Math.cos(angle) * speed;
    double vy = Math.sin(angle) * speed;
    projectiles.add(new Projectile(player.x, player.y, vx, vy, damage, radius));
}
