private void resetRun() {
    gameState = GameState.PLAYING;
    upgradeState = UpgradeState.NONE;
    worldTime = 0;
    wave = 1;
    waveTimer = 0;
    score = 0;
    pendingLevelUps = 0;
    enemies.clear();
    projectiles.clear();
    xpOrbs.clear();
    damageNumbers.clear();
    unlockedWeapons.clear();
    unlockedWeapons.add(WeaponType.MAGIC_BOLT);
    player.reset();
}

// keyPressed: GAME_OVER + R → resetRun()
