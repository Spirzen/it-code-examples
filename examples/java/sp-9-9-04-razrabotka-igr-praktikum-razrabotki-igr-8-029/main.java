double bossTimer = 120;

private void updateWaveAndBoss(double dt) {
    waveTimer += dt;
    if (waveTimer >= 30) {
        waveTimer = 0;
        wave++;
    }
    bossTimer -= dt;
    if (bossTimer <= 0) {
        bossTimer = 120;
        enemies.add(spawnBoss());
    }
}

private Enemy spawnBoss() {
    Enemy boss = new Enemy(WIDTH / 2.0, -60, 36, 800 + wave * 50, 55, 40);
    boss.kind = EnemyKind.BOSS;
    return boss;
}
