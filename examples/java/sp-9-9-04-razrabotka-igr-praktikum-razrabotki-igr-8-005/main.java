package com.survivors;

public final class Player {
    public double x = 480;
    public double y = 270;
    public double radius = 16;
    public double maxHp = 100;
    public double hp = 100;
    public double moveSpeed = 220;

    public void updateMovement(double dt, boolean up, boolean down,
                               boolean left, boolean right, int maxW, int maxH,
                               double speedMultiplier) {
        double dx = 0, dy = 0;
        if (up) dy -= 1;
        if (down) dy += 1;
        if (left) dx -= 1;
        if (right) dx += 1;
        if (dx == 0 && dy == 0) return;
        double len = Math.hypot(dx, dy);
        x += (dx / len) * moveSpeed * speedMultiplier * dt;
        y += (dy / len) * moveSpeed * speedMultiplier * dt;
        x = Math.max(radius, Math.min(maxW - radius, x));
        y = Math.max(radius, Math.min(maxH - radius, y));
    }
}
