UpgradeState upgradeState = UpgradeState.NONE;
final List<String> upgradeChoices = new ArrayList<>();
int pendingLevelUps = 0;

// в конце update, если pendingLevelUps > 0 и upgradeState == NONE:
//   upgradeState = PAUSED_FOR_UPGRADE;
//   rollUpgradeChoices();

private void rollUpgradeChoices() {
    upgradeChoices.clear();
    List<String> pool = List.of(
            "Сила +20%", "Скорость атаки +20%", "Макс. HP +25",
            "Магнит +25%", "Скорость движения +15%", "Урон +5");
    List<String> copy = new ArrayList<>(pool);
    for (int i = 0; i < 3 && !copy.isEmpty(); i++) {
        int idx = rng.nextInt(copy.size());
        upgradeChoices.add(copy.remove(idx));
    }
}

private void applyUpgrade(String choice) {
    switch (choice) {
        case "Сила +20%" -> player.damageMultiplier *= 1.2;
        case "Скорость атаки +20%" -> player.attackSpeedMultiplier *= 1.2;
        case "Макс. HP +25" -> { player.maxHp += 25; player.hp += 25; }
        case "Магнит +25%" -> player.magnetRadius *= 1.25;
        case "Скорость движения +15%" -> player.moveSpeed *= 1.15;
        case "Урон +5" -> player.flatDamageBonus += 5;
        default -> { }
    }
}
