buildSidebar
	| title origin labels button |
	sidebarButtons := Dictionary new.
	title := StringMorph contents: 'SmallDesktop' font: (TextStyle default fontOfSize: 18).
	title color: Color white.
	self addMorph: title.
	title position: 16 @ 16.

	labels := #(
		(#notes 'Заметки')
		(#calculator 'Калькулятор')
		(#about 'О программе')
		(#settings 'Настройки')
	).
	origin := 12 @ 56.
	labels do: [ :pair |
		button := SimpleButtonMorph new.
		button label: pair second; font: (TextStyle default fontOfSize: 13).
		button target: self; actionSelector: #sidebarClicked:.
		button setProperty: #desktopSection toValue: pair first.
		button extent: 136 @ 28.
		button position: origin.
		self addMorph: button.
		sidebarButtons at: pair first put: button.
		origin := origin + (0 @ 34) ]
