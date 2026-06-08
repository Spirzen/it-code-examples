initialize
    super initialize.
    fieldWidth := 480.
    fieldHeight := 640.
    playerWidth := 28.
    playerHeight := 22.
    playerSpeed := 6.
    playerLives := 3.
    shootTimer := 0.
    invulnerableTimer := 0.
    tickCount := 0.
    highScore := 0.
    paused := false.
    self resetGame
