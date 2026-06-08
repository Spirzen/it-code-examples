private Enemy spawnEnemy() {
    double side = rng.nextDouble();
    double x, y;
    if (side < 0.25) { x = -50; y = rng.nextDouble() * HEIGHT; }
    else if (side < 0.5) { x = WIDTH + 50; y = rng.nextDouble() * HEIGHT; }
    else if (side < 0.75) { x = rng.nextDouble() * WIDTH; y = -50; }
    else { x = rng.nextDouble() * WIDTH; y = HEIGHT + 50; }

    double t = worldTime;
    double difficulty = 1.0 + (t * 0.018) + (Math.pow(t, 1.18) * 0.0012);
    double roll = rng.nextDouble();

    if (roll < 0.12) {
        Enemy e = new Enemy(x, y, 10, 26 * difficulty, 190 + difficulty * 14, 2);
        e.kind = EnemyKind.SPEEDER;
        return e;
    }
    if (roll < 0.26) {
        Enemy e = new Enemy(x, y, 14, 40 * difficulty, 105 + difficulty * 8, 3);
        e.kind = EnemyKind.SHOOTER;
        return e;
    }
    if (roll < 0.48) {
        Enemy e = new Enemy(x, y, 22, 95 * difficulty, 62 + difficulty * 5, 4);
        e.kind = EnemyKind.TANK;
        return e;
    }
    return new Enemy(x, y, 14, 40 * difficulty, 105 + difficulty * 8, 2);
}
