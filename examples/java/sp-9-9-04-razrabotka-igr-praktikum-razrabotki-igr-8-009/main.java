package com.survivors;

public final class Projectile {
    public double x, y;
    public final double vx, vy;
    public double damage;
    public double radius;
    public double life = 1.5;

    public Projectile(double x, double y, double vx, double vy, double damage, double radius) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.damage = damage;
        this.radius = radius;
    }
}
