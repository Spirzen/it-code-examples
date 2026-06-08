moveAt: anIndex
	| lines |
	(self canMoveAt: anIndex) ifFalse: [ ^ false ].
	board at: anIndex put: currentPlayer.
	lines := #(
		(1 2 3) (4 5 6) (7 8 9)
		(1 4 7) (2 5 8) (3 6 9)
		(1 5 9) (3 5 7)
	).
	lines do: [ :line |
		| a b c |
		a := board at: line first.
		b := board at: line second.
		c := board at: line third.
		(a notNil and: [ a = b and: [ b = c ] ]) ifTrue: [
			winner := a.
			gameOver := true.
			^ true ] ].
	(board allSatisfy: [ :each | each notNil ]) ifTrue: [
		gameOver := true ].
	currentPlayer := currentPlayer = #X ifTrue: [ #O ] ifFalse: [ #X ].
	^ true
