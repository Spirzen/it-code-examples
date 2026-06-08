sidebarClicked: aButton
	| section |
	section := aButton getProperty: #desktopSection.
	self showSection: section

showSection: aSymbol
	currentSection := aSymbol.
	notesPanel visible: (aSymbol = #notes).
	calculatorPanel visible: (aSymbol = #calculator).
	aboutPanel visible: (aSymbol = #about).
	settingsPanel visible: (aSymbol = #settings).
	sidebarButtons keysAndValuesDo: [ :key :button |
		button color: (key = aSymbol
			ifTrue: [ accentColor ]
			ifFalse: [ (darkTheme ifTrue: [ Color gray darker ] ifFalse: [ Color lightGray ]) ]) ].
	self refreshStatusBar
