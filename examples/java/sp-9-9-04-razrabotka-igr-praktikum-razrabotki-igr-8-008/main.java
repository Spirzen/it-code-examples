import java.util.ArrayList;
import java.util.List;
import java.util.Random;

final List<Enemy> enemies = new ArrayList<>();
final Random rng = new Random();
double spawnTimer = 0;
double worldTime = 0;

private void update(double dt) {
    if (gameState != GameState.PLAYING) return;
    worldTime += dt;
    player.updateMovement(dt, up, down, left, right, WIDTH, HEIGHT, 1.0);

    spawnTimer -= dt;
    if (spawnTimer <= 0) {
        spawnTimer = Math.max(0.15, 0.9 - worldTime * 0.004);
        enemies.add(spawnEnemy());
    }
    updateEnemies(dt);
}

private Enemy spawnEnemy() {
    double side = rng.nextDouble();
    double x, y;
    if (side < 0.25) { x = -40; y = rng.nextDouble() * HEIGHT; }
    else if (side < 0.5) { x = WIDTH + 40; y = rng.nextDouble() * HEIGHT; }
    else if (side < 0.75) { x = rng.nextDouble() * WIDTH; y = -40; }
    else { x = rng.nextDouble() * WIDTH; y = HEIGHT + 40; }
    double diff = 1.0 + worldTime * 0.02;
    return new Enemy(x, y, 14, 35 * diff, 90 + diff * 10, 2);
}

private void updateEnemies(double dt) {
    for (Enemy e : enemies) {
        double dx = player.x - e.x;
        double dy = player.y - e.y;
        double len = Math.hypot(dx, dy);
        if (len > 0.001) {
            e.x += (dx / len) * e.speed * dt;
            e.y += (dy / len) * e.speed * dt;
        }
    }
}
