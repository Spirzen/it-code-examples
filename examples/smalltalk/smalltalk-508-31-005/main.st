step
	| leftRect rightRect ballRect relativeHit |
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
		ballVY := ballVY abs negated ].
	leftRect := self leftPaddleOrigin extent: self paddleExtent.
	rightRect := self rightPaddleOrigin extent: self paddleExtent.
	ballRect := ballX @ ballY extent: ballSize @ ballSize.
	(ballVX < 0 and: [ leftRect intersects: ballRect ]) ifTrue: [
		ballX := leftRect right + 1.
		relativeHit := ((ballY + (ballSize / 2)) - leftPaddleY) / paddleHeight - 0.5.
		ballVY := relativeHit * ballSpeed * 1.6.
		ballVX := ballSpeed abs ].
	(ballVX > 0 and: [ rightRect intersects: ballRect ]) ifTrue: [
		ballX := rightRect left - ballSize - 1.
		relativeHit := ((ballY + (ballSize / 2)) - rightPaddleY) / paddleHeight - 0.5.
		ballVY := relativeHit * ballSpeed * 1.6.
		ballVX := ballSpeed abs negated ].
	(ballX + ballSize < 0) ifTrue: [
		rightScore := rightScore + 1.
		self checkWinFor: #Right.
		self resetBall ].
	(ballX > fieldWidth) ifTrue: [
		leftScore := leftScore + 1.
		self checkWinFor: #Left.
		self resetBall ]
