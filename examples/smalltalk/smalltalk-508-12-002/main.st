buildUI
	| cellSize gap origin |
	statusMorph := StringMorph contents: game statusText font: (TextStyle default fontOfSize: 18).
	statusMorph color: Color black.
	self addMorph: statusMorph.
	statusMorph position: 10 @ 10.

	newGameButton := SimpleButtonMorph new.
	newGameButton label: 'Новая игра'; font: (TextStyle default fontOfSize: 14).
	newGameButton target: self; actionSelector: #newGame.
	self addMorph: newGameButton.
	newGameButton position: 220 @ 8.

	cellMorphs := OrderedCollection new.
	cellSize := 80.
	gap := 4.
	origin := 10 @ 45.
	1 to: 9 do: [ :i |
		| cell row col |
		row := (i - 1) // 3.
		col := (i - 1) \\ 3.
		cell := TTTCellMorph new initializeBoard: self at: i.
		cell extent: cellSize @ cellSize.
		cell position: origin + ((col * (cellSize + gap)) @ (row * (cellSize + gap))).
		self addMorph: cell.
		cellMorphs add: cell ].
	self extent: 270 @ 320
