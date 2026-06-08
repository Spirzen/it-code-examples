ballPosition
	^ ballX @ ballY

fieldExtent
	^ fieldWidth @ fieldHeight

paddleExtent
	^ paddleWidth @ paddleHeight

leftPaddleOrigin
	^ 10 @ leftPaddleY

rightPaddleOrigin
	^ (fieldWidth - 10 - paddleWidth) @ rightPaddleY

leftScore
	^ leftScore

rightScore
	^ rightScore

paused
	^ paused

gameOver
	^ gameOver

winner
	^ winner
