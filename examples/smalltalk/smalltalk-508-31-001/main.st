resetGame
	leftScore := 0.
	rightScore := 0.
	gameOver := false.
	winner := nil.
	paused := false.
	leftUp := false.
	leftDown := false.
	rightUp := false.
	rightDown := false.
	self resetPaddles.
	self resetBall

resetPaddles
	leftPaddleY := fieldHeight // 2 - (paddleHeight // 2).
	rightPaddleY := leftPaddleY

resetBall
	| direction |
	ballX := fieldWidth // 2 - (ballSize // 2).
	ballY := fieldHeight // 2 - (ballSize // 2).
	direction := #( -1 1 ) atRandom.
	ballVX := ballSpeed * direction.
	ballVY := ballSpeed * (#( -1 1 ) atRandom)
