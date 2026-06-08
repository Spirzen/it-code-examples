resetGame
    score := 0.
    waveNumber := 0.
    waveState := #break.
    waveBreakTimer := 60.
    spawnIndex := 1.
    spawnQueue := OrderedCollection new.
    spawnDelayTimer := 0.
    bullets := OrderedCollection new.
    enemies := OrderedCollection new.
    gameOver := false.
    paused := false.
    movingLeft := false.
    movingRight := false.
    shootTimer := 0.
    invulnerableTimer := 0.
    tickCount := 0.
    self resetPlayer

resetPlayer
    playerX := fieldWidth // 2 - (playerWidth // 2).
    playerY := fieldHeight - playerHeight - 24.
    playerLives := 3.
    invulnerableTimer := 90

scoreText
    ^ 'Счёт: ', score asString, '  Волна: ', waveNumber asString, '  Жизни: ', playerLives asString

statusText
    gameOver ifTrue: [ ^ 'Игра окончена! Нажмите "Новая игра" или R' ].
    paused ifTrue: [ ^ 'Пауза (P — продолжить)' ].
    waveState = #break ifTrue: [ ^ 'Готовься к волне ', (waveNumber + 1) asString, '!' ].
    ^ '←/→ или A/D — движение, пробел — огонь, P — пауза'

step
    gameOver ifTrue: [ ^ self ].
    paused ifTrue: [ ^ self ].
    tickCount := tickCount + 1
