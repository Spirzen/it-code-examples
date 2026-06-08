initialize
    super initialize.
    self color: Color black.
    game := ShooterGame new.
    pressedKeys := Set new.
    spaceHeld := false.
    playfieldOrigin := 10 @ 50.
    self buildUI.
    self startStepping

buildUI
    | fieldExtent |
    fieldExtent := game fieldExtent.
    playfieldMorph := ShooterPlayfieldMorph new initializeWithGame: game.
    playfieldMorph extent: fieldExtent.
    playfieldMorph position: playfieldOrigin.
    self addMorph: playfieldMorph.
    self extent: (fieldExtent x + 20) @ (fieldExtent y + 60).
    scoreMorph := StringMorph contents: game scoreText font: (TextStyle default fontOfSize: 16).
    scoreMorph color: Color white.
    self addMorph: scoreMorph.
    scoreMorph position: 10 @ 10.
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
