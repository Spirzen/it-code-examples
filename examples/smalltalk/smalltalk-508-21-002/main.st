computePending
	| left right result |
	left := pendingValue.
	right := display asNumber.
	result := pendingOperator = #+
		ifTrue: [ left + right ]
		ifFalse: [
			pendingOperator = #-
				ifTrue: [ left - right ]
				ifFalse: [
					pendingOperator = #*
						ifTrue: [ left * right ]
						ifFalse: [
							right ~= 0
								ifTrue: [ left / right ]
								ifFalse: [ left ] ] ] ].
	display := result printString.
	pendingValue := result
