fieldExtent
    ^ fieldWidth @ fieldHeight

playerOrigin
    ^ playerX @ playerY

playerSize
    ^ playerWidth @ playerHeight

bulletsList
    ^ bullets

enemiesList
    ^ enemies

score
    ^ score

lives
    ^ playerLives

wave
    ^ waveNumber

tickCount
    ^ tickCount

invulnerable
    ^ invulnerableTimer > 0

gameOver
    ^ gameOver

paused
    ^ paused
