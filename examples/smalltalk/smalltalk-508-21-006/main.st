buildNotesPanel
	| panel title inputRow addButton clearButton |
	panel := BorderedMorph new.
	panel color: Color white.
	panel borderWidth: 1.
	panel borderColor: (Color gray alpha: 0.35).
	panel extent: 430 @ 390.

	title := StringMorph contents: 'Заметки' font: (TextStyle default fontOfSize: 20).
	title color: Color black.
	panel addMorph: title.
	title position: 16 @ 12.

	noteInputModel := TextModel new.
	noteInputMorph := PluggableTextMorph on: noteInputModel textColor: Color black.
	noteInputMorph extent: 280 @ 24.
	panel addMorph: noteInputMorph.
	noteInputMorph position: 16 @ 48.

	addButton := SimpleButtonMorph new.
	addButton label: 'Добавить'; font: (TextStyle default fontOfSize: 13).
	addButton target: self; actionSelector: #addNote.
	panel addMorph: addButton.
	addButton position: 306 @ 46.

	clearButton := SimpleButtonMorph new.
	clearButton label: 'Очистить всё'; font: (TextStyle default fontOfSize: 13).
	clearButton target: self; actionSelector: #clearNotes.
	panel addMorph: clearButton.
	clearButton position: 16 @ 82.

	noteListMorph := Morph new.
	noteListMorph color: Color transparent.
	noteListMorph extent: 398 @ 280.
	panel addMorph: noteListMorph.
	noteListMorph position: 16 @ 118.
	^ panel
