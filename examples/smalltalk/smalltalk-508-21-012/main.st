useLightTheme
	darkTheme := false.
	self applyTheme

useDarkTheme
	darkTheme := true.
	self applyTheme

applyTheme
	| sidebarColor panelColor textColor |
	sidebarColor := darkTheme ifTrue: [ Color r: 0.12 g: 0.14 b: 0.18 ] ifFalse: [ Color r: 0.93 g: 0.94 b: 0.96 ].
	panelColor := darkTheme ifTrue: [ Color r: 0.18 g: 0.2 b: 0.24 ] ifFalse: [ Color white ].
	textColor := darkTheme ifTrue: [ Color white ] ifFalse: [ Color black ].
	self color: sidebarColor.
	self submorphsDo: [ :m |
		(m isKindOf: StringMorph and: [ m contents = 'SmallDesktop' ]) ifTrue: [
			m color: textColor ] ].
	{ notesPanel. calculatorPanel. aboutPanel. settingsPanel } do: [ :panel |
		panel color: panelColor.
		panel borderColor: (darkTheme ifTrue: [ Color gray darker ] ifFalse: [ Color gray alpha: 0.35 ]).
		panel submorphsDo: [ :m |
			m isKindOf: StringMorph ifTrue: [ m color: textColor ] ] ].
	statusMorph color: textColor.
	clockMorph color: textColor.
	self showSection: currentSection
