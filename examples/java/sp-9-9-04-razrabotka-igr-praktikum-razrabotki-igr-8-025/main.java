private void update(double dt) {
    if (gameState == GameState.MENU || gameState == GameState.GAME_OVER) {
        return;
    }
    if (upgradeState == UpgradeState.PAUSED_FOR_UPGRADE) {
        return;
    }

    worldTime += dt;
    updateWaveAndBoss(dt);

    if (isDashing) { /* dashTimer */ } else { dashCooldownTimer -= dt; }

    player.heal(dt);
    player.updateMovement(dt, up, down, left, right, WIDTH, HEIGHT, isDashing ? DASH_SPEED_MULT : 1.0);

    updateWeapons(dt);
    spawnEnemies(dt);
    updateEnemies(dt);
    updateProjectiles(dt);
    updateXpOrbs(dt);
    updateParticles(dt);
    updateDamageNumbers(dt);
    updateContactDamage(dt);

    if (pendingLevelUps > 0 && upgradeState == UpgradeState.NONE) {
        upgradeState = UpgradeState.PAUSED_FOR_UPGRADE;
        rollUpgradeChoices();
    }
}
