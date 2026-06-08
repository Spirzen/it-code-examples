package com.survivors;

import java.awt.*;

public final class DamageNumber {
    public double x, y;
    public String text;
    public double life = 0.8;
    public Color color = new Color(255, 230, 120);

    public DamageNumber(double x, double y, String text) {
        this.x = x; this.y = y; this.text = text;
    }
}
