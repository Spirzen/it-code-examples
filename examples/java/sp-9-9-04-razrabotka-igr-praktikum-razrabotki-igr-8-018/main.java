final Set<WeaponType> unlockedWeapons = new EnumSet<>(EnumSet.of(WeaponType.MAGIC_BOLT));

void updateWeapons(double dt) {
    if (enemies.isEmpty()) return;
    if (unlockedWeapons.contains(WeaponType.MAGIC_BOLT)) {
        player.shotCooldown -= dt;
        if (player.shotCooldown <= 0) {
            shootMagicBolt();
            player.shotCooldown = Math.max(0.08, 0.35 / player.attackSpeedMultiplier);
        }
    }
    if (unlockedWeapons.contains(WeaponType.TRIPLE_CAST)) {
        player.tripleCooldown -= dt;
        if (player.tripleCooldown <= 0) {
            shootTripleCast();
            player.tripleCooldown = Math.max(0.2, 1.0 / player.attackSpeedMultiplier);
        }
    }
    if (unlockedWeapons.contains(WeaponType.PULSE_RING)) {
        player.pulseCooldown -= dt;
        if (player.pulseCooldown <= 0) {
            shootPulseRing();
            player.pulseCooldown = Math.max(0.5, 2.0 / player.attackSpeedMultiplier);
        }
    }
}
