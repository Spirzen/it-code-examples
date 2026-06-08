double contactDamageTimer = 0;

// в update:
player.heal(dt);
contactDamageTimer -= dt;
if (contactDamageTimer <= 0) {
    double sum = 0;
    for (Enemy e : enemies) {
        if (circlesHit(player.x, player.y, player.radius, e.x, e.y, e.radius)) {
            sum += 3.5;
        }
    }
    if (sum > 0) {
        double incoming = sum * (1.0 - player.armorReduction);
        player.hp -= incoming;
        contactDamageTimer = 0.25;
        if (player.hp <= 0) {
            player.hp = 0;
            gameState = GameState.GAME_OVER;
        }
    }
}
