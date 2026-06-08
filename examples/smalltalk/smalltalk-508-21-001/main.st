digit: aCharacter
	| digit |
	digit := aCharacter asString.
	freshEntry ifTrue: [
		display := digit = '0' ifTrue: [ '0' ] ifFalse: [ digit ].
		freshEntry := false ]
	ifFalse: [
		display := display = '0'
			ifTrue: [ digit ]
			ifFalse: [ display, digit ] ]

decimalPoint
	freshEntry ifTrue: [
		display := '0.'.
		freshEntry := false ]
	ifFalse: [
		(display includes: $.) ifFalse: [
			display := display, '.' ] ]

toggleSign
	display := (display asNumber negated) asString
