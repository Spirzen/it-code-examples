buildSettingsPanel
	| panel title lightButton darkButton hint |
	panel := BorderedMorph new.
	panel color: Color white.
	panel borderWidth: 1.
	panel borderColor: (Color gray alpha: 0.35).
	panel extent: 430 @ 390.

	title := StringMorph contents: 'Настройки' font: (TextStyle default fontOfSize: 20).
	title color: Color black.
	panel addMorph: title.
	title position: 16 @ 12.

	lightButton := SimpleButtonMorph new.
	lightButton label: 'Светлая тема'; font: (TextStyle default fontOfSize: 13).
	lightButton target: self; actionSelector: #useLightTheme.
	panel addMorph: lightButton.
	lightButton position: 16 @ 56.

	darkButton := SimpleButtonMorph new.
	darkButton label: 'Тёмная тема'; font: (TextStyle default fontOfSize: 13).
	darkButton target: self; actionSelector: #useDarkTheme.
	panel addMorph: darkButton.
	darkButton position: 140 @ 56.

	hint := StringMorph contents: 'Тема меняет цвет фона окна и боковой панели.' font: (TextStyle default fontOfSize: 13).
	hint color: Color gray.
	panel addMorph: hint.
	hint position: 16 @ 100.
	^ panel
