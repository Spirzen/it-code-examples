calcButtonPressed: aButton
	| label |
	label := aButton getProperty: #calcLabel.
	(label size = 1 and: [ label first isDigit ]) ifTrue: [
		calculator digit: label first ].
	label = '.' ifTrue: [ calculator decimalPoint ].
	label = '±' ifTrue: [ calculator toggleSign ].
	label = 'C' ifTrue: [ calculator clear ].
	label = '=' ifTrue: [ calculator equals ].
	label = '+' ifTrue: [ calculator operator: #+ ].
	label = '-' ifTrue: [ calculator operator: #- ].
	label = '*' ifTrue: [ calculator operator: #* ].
	label = '/' ifTrue: [ calculator operator: #/ ].
	self refreshCalculatorDisplay

refreshCalculatorDisplay
	calculatorPanel submorphsDo: [ :each |
		(each hasProperty: #calcDisplay) ifTrue: [
			each contents: calculator displayText ] ]
