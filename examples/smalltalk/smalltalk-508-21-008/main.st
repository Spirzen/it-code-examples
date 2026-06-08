buildCalculatorPanel
	| panel title displayMorph rows origin rowLabels button |
	panel := BorderedMorph new.
	panel color: Color white.
	panel borderWidth: 1.
	panel borderColor: (Color gray alpha: 0.35).
	panel extent: 430 @ 390.

	title := StringMorph contents: 'Калькулятор' font: (TextStyle default fontOfSize: 20).
	title color: Color black.
	panel addMorph: title.
	title position: 16 @ 12.

	displayMorph := StringMorph contents: calculator displayText font: (TextStyle default fontOfSize: 24).
	displayMorph color: Color black.
	displayMorph setProperty: #calcDisplay toValue: true.
	panel addMorph: displayMorph.
	displayMorph extent: 280 @ 28.
	displayMorph position: 16 @ 48.

	rows := #(
		#('7' '8' '9' '/')
		#('4' '5' '6' '*')
		#('1' '2' '3' '-')
		#('0' '.' '±' '+')
		#('C' '=')
	).
	origin := 16 @ 92.
	rows do: [ :rowLabels |
		origin := 16 @ origin y.
		rowLabels do: [ :label |
			button := SimpleButtonMorph new.
			button label: label; font: (TextStyle default fontOfSize: 14).
			button extent: 64 @ 36.
			button position: origin.
			button target: self; actionSelector: #calcButtonPressed:.
			button setProperty: #calcLabel toValue: label.
			panel addMorph: button.
			origin := origin + (72 @ 0) ].
		origin := origin + (0 @ 44) ].
	^ panel
