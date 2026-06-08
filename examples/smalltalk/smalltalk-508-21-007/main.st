addNote
	noteStore addNote: noteInputModel contents ifTrue: [
		noteInputModel contents: ''.
		self refreshNotes ]

clearNotes
	noteStore clearAll.
	self refreshNotes

deleteNoteAt: anIndex
	noteStore removeAt: anIndex.
	self refreshNotes

refreshNotes
	| origin index |
	noteListMorph removeAllMorphs.
	origin := 0 @ 0.
	index := 1.
	noteStore allNotes do: [ :each |
		| row |
		row := DesktopNoteRowMorph new initializeApp: self at: index text: each.
		row extent: 370 @ 28.
		row position: origin.
		noteListMorph addMorph: row.
		origin := origin + (0 @ 32).
		index := index + 1 ].
	self refreshStatusBar
