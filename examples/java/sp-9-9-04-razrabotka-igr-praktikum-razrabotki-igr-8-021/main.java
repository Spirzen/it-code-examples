boolean isDashing = false;
double dashTimer = 0;
double dashCooldownTimer = 0;
static final double DASH_DURATION = 0.15;
static final double DASH_COOLDOWN = 1.4;
static final double DASH_SPEED_MULT = 4.0;

// keyPressed — внутри PLAYING:
if (e.getKeyCode() == KeyEvent.VK_SPACE && !isDashing && dashCooldownTimer <= 0) {
    isDashing = true;
    dashTimer = DASH_DURATION;
    dashCooldownTimer = DASH_COOLDOWN;
}

// в update после движения:
if (isDashing) {
    dashTimer -= dt;
    if (dashTimer <= 0) {
        isDashing = false;
    }
} else if (dashCooldownTimer > 0) {
    dashCooldownTimer -= dt;
}

// в updateMovement Player или в GamePanel перед вызовом player.updateMovement:
double speedMult = isDashing ? DASH_SPEED_MULT : 1.0;
// передайте speedMult в расчёт смещения (умножьте moveSpeed на speedMult)

// контактный урон — только если !isDashing
