buildAboutPanel
	| panel title text |
	panel := BorderedMorph new.
	panel color: Color white.
	panel borderWidth: 1.
	panel borderColor: (Color gray alpha: 0.35).
	panel extent: 430 @ 390.

	title := StringMorph contents: 'О программе' font: (TextStyle default fontOfSize: 20).
	title color: Color black.
	panel addMorph: title.
	title position: 16 @ 12.

	text := StringMorph contents:
		'SmallDesktop — демонстрационное настольное приложение на Pharo Morphic.' , String cr ,
		String cr ,
		'В приложении показаны типичные элементы интерфейса:' , String cr ,
		'• боковая панель навигации' , String cr ,
		'• поле ввода текста и список заметок' , String cr ,
		'• кнопки действий' , String cr ,
		'• простой калькулятор' , String cr ,
		'• переключение светлой и тёмной темы' , String cr ,
		'• строка статуса с часами' font: (TextStyle default fontOfSize: 14).
	text color: Color darkGray.
	panel addMorph: text.
	text position: 16 @ 52.
	^ panel
