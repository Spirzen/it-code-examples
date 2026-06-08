handlesKeyboard: evt
	^ true

handleKeyDown: anEvent
	| keyName |
	keyName := anEvent keyName.
	pressedKeys add: keyName.
	keyName = ' ' ifTrue: [ game togglePause ].
	self syncInput

handleKeyUp: anEvent
	pressedKeys remove: anEvent keyName ifAbsent: [].
	self syncInput

keydown: anEvent
	self handleKeyDown: anEvent

keyup: anEvent
	self handleKeyUp: anEvent

syncInput
	game
		leftUp: ((pressedKeys includes: 'W') or: [ pressedKeys includes: 'w' ]);
		leftDown: ((pressedKeys includes: 'S') or: [ pressedKeys includes: 's' ]);
		rightUp: (pressedKeys includes: 'ArrowUp');
		rightDown: (pressedKeys includes: 'ArrowDown')
