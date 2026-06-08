private void pickUpgrade(int index) {
    if (index < 0 || index >= upgradeChoices.size()) return;
    applyUpgrade(upgradeChoices.get(index));
    pendingLevelUps--;
    if (pendingLevelUps > 0) {
        rollUpgradeChoices();
    } else {
        upgradeState = UpgradeState.NONE;
        upgradeChoices.clear();
    }
}

// в конце update (после XP), когда pendingLevelUps > 0:
if (pendingLevelUps > 0 && upgradeState == UpgradeState.NONE) {
    upgradeState = UpgradeState.PAUSED_FOR_UPGRADE;
    rollUpgradeChoices();
}
