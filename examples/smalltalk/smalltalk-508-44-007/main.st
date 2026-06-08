handlesKeyboard: evt
    ^ true

handleKeyDown: anEvent
    | keyName |
    keyName := anEvent keyName.
    pressedKeys add: keyName.
    self syncInput

handleKeyUp: anEvent
    | keyName |
    keyName := anEvent keyName.
    pressedKeys remove: keyName ifAbsent: [].
    self syncInput

keydown: anEvent
    self handleKeyDown: anEvent

keyup: anEvent
    self handleKeyUp: anEvent

syncInput
    game
        movingLeft: ((pressedKeys includes: 'ArrowLeft') or: [ pressedKeys includes: 'a' ] or: [ pressedKeys includes: 'A' ]);
        movingRight: ((pressedKeys includes: 'ArrowRight') or: [ pressedKeys includes: 'd' ] or: [ pressedKeys includes: 'D' ])
