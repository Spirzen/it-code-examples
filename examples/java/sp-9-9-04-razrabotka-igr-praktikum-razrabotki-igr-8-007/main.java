package com.survivors;

public final class Enemy {
    public double x, y;
    public final double radius;
    public double hp;
    public final double speed;
    public final int xpValue;

    public Enemy(double x, double y, double radius, double hp, double speed, int xpValue) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.hp = hp;
        this.speed = speed;
        this.xpValue = xpValue;
    }
}
