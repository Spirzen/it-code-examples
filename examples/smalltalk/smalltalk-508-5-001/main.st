Object subclass: #Stack
    instanceVariableNames: 'contents'
    package: 'Examples'

Stack >> initialize
    contents := OrderedCollection new.

Stack >> push: anObject
    contents addLast: anObject.

Stack >> pop
    ^ contents removeLast.

Stack >> isEmpty
    ^ contents isEmpty.
