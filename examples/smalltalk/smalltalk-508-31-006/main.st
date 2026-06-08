initialize
	super initialize.
	self color: Color black.
	game := PongGame new.
	pressedKeys := Set new.
	playfieldOrigin := 10 @ 50.
	self buildUI

buildUI
	| fieldExtent |
	fieldExtent := game fieldExtent.
	playfieldMorph := PongPlayfieldMorph new.
	playfieldMorph color: (Color r: 0.05 g: 0.12 b: 0.05).
	playfieldMorph extent: fieldExtent.
	playfieldMorph position: playfieldOrigin.
	self addMorph: playfieldMorph.

	leftPaddleMorph := Morph new.
	leftPaddleMorph color: Color white.
	leftPaddleMorph extent: game paddleExtent.
	self addMorph: leftPaddleMorph.

	rightPaddleMorph := Morph new.
	rightPaddleMorph color: Color white.
	rightPaddleMorph extent: game paddleExtent.
	self addMorph: rightPaddleMorph.

	ballMorph := Morph new.
	ballMorph color: Color yellow.
	ballMorph extent: game ballSize @ game ballSize.
	self addMorph: ballMorph.

	self extent: (fieldExtent x + 20) @ (fieldExtent y + 60).

	scoreMorph := StringMorph contents: game scoreText font: (TextStyle default fontOfSize: 24).
	scoreMorph color: Color white.
	self addMorph: scoreMorph.
	scoreMorph position: (fieldExtent x // 2 - 10) @ 10.

	statusMorph := StringMorph contents: game statusText font: (TextStyle default fontOfSize: 12).
	statusMorph color: Color lightGray.
	self addMorph: statusMorph.
	statusMorph position: 10 @ 28.

	newGameButton := SimpleButtonMorph new.
	newGameButton label: 'Новая игра'; font: (TextStyle default fontOfSize: 14).
	newGameButton target: self; actionSelector: #newGame.
	self addMorph: newGameButton.
	newGameButton position: (fieldExtent x - 90) @ 8.
	self refreshDisplay
