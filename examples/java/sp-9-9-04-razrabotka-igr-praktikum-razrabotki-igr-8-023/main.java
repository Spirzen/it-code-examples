final List<Particle> particles = new ArrayList<>();

private void spawnKillParticles(double x, double y) {
    for (int i = 0; i < 8; i++) {
        double a = rng.nextDouble() * Math.PI * 2;
        double sp = 80 + rng.nextDouble() * 120;
        particles.add(new Particle(x, y,
                Math.cos(a) * sp, Math.sin(a) * sp,
                GameColors.ENEMY));
    }
}

private void updateParticles(double dt) {
    Iterator<Particle> it = particles.iterator();
    while (it.hasNext()) {
        Particle p = it.next();
        p.x += p.vx * dt;
        p.y += p.vy * dt;
        p.life -= dt;
        if (p.life <= 0) it.remove();
    }
}
