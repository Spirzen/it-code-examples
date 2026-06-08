step
	gameOver ifTrue: [ ^ self ].
	paused ifTrue: [ ^ self ].
	leftUp ifTrue: [
		leftPaddleY := (leftPaddleY - paddleSpeed) max: 0 ].
	leftDown ifTrue: [
		leftPaddleY := (leftPaddleY + paddleSpeed) min: fieldHeight - paddleHeight ].
	rightUp ifTrue: [
		rightPaddleY := (rightPaddleY - paddleSpeed) max: 0 ].
	rightDown ifTrue: [
		rightPaddleY := (rightPaddleY + paddleSpeed) min: fieldHeight - paddleHeight ].
	ballX := ballX + ballVX.
	ballY := ballY + ballVY.
	(ballY <= 0) ifTrue: [
		ballY := 0.
		ballVY := ballVY abs ].
	(ballY + ballSize >= fieldHeight) ifTrue: [
		ballY := fieldHeight - ballSize.
		ballVY := ballVY abs negated ]
