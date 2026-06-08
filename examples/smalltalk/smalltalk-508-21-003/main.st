initializeApp: anAppMorph at: anIndex text: aString
	appMorph := anAppMorph.
	index := anIndex.
	self color: Color white.
	self borderWidth: 1.
	self borderColor: (Color gray alpha: 0.4).
	labelMorph := StringMorph contents: aString font: (TextStyle default fontOfSize: 14).
	labelMorph color: Color black.
	self addMorph: labelMorph.
	labelMorph position: 8 @ 6.
	deleteButton := SimpleButtonMorph new.
	deleteButton label: '×'; font: (TextStyle default fontOfSize: 14).
	deleteButton target: self; actionSelector: #deleteClicked.
	self addMorph: deleteButton.
	deleteButton position: 330 @ 2
