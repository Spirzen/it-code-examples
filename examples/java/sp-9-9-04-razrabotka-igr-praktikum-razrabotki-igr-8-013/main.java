private void updateXpOrbs(double dt) {
    Iterator<XpOrb> it = xpOrbs.iterator();
    while (it.hasNext()) {
        XpOrb o = it.next();
        double dx = player.x - o.x;
        double dy = player.y - o.y;
        double d = Math.hypot(dx, dy);
        if (d < player.magnetRadius && d > 1) {
            double pull = 320 * dt;
            o.x += (dx / d) * pull;
            o.y += (dy / d) * pull;
        }
        if (d < player.radius + 8) {
            addXp(o.value);
            it.remove();
        }
    }
}

private void addXp(int amount) {
    player.xp += amount;
    while (player.xp >= player.xpToNext) {
        player.xp -= player.xpToNext;
        player.level++;
        player.xpToNext = (int) (player.xpToNext * 1.25) + 4;
        pendingLevelUps++;
    }
}
