void spawnEnemies(double dt) {
    spawnTimer -= dt;
    if (spawnTimer > 0) return;

    double t = worldTime;
    double difficulty = 1.0 + (t * 0.018) + (Math.pow(t, 1.18) * 0.0012);
    int batch = 1 + (int) Math.floor(t / 45.0);
    if (rng.nextDouble() < Math.min(0.55, 0.20 + t / 260.0)) {
        batch++;
    }
    spawnTimer = Math.max(0.08, 0.78 - (t * 0.0038));

    for (int i = 0; i < batch; i++) {
        enemies.add(spawnEnemy(difficulty));
    }
}
