enemySpeed
    ^ 1.5 + (waveNumber * 0.15)

enemySizeFor: aType
    aType = #grunt ifTrue: [ ^ 24 @ 20 ].
    aType = #zigzag ifTrue: [ ^ 22 @ 18 ].
    ^ 26 @ 22

enemyHpFor: aType
    aType = #shooter ifTrue: [ ^ 2 ].
    ^ 1

addEnemyAt: aPoint type: aType
    enemies add: {
        aPoint x.
        aPoint y.
        aType.
        self enemyHpFor: aType.
        (80 + 120 atRandom) - (waveNumber * 3 max: 0).
        tickCount + (aPoint x asFloat / 8)
    }

updateEnemies
    | toRemove enemy type size speed x y |
    toRemove := OrderedCollection new.
    speed := self enemySpeed.
    enemies do: [ :each |
        enemy := each.
        type := enemy third.
        size := self enemySizeFor: type.
        x := enemy first.
        y := enemy second + speed.
        enemy at: 1 put: x.
        enemy at: 2 put: y.
        (y > fieldHeight + 40) ifTrue: [ toRemove add: enemy ] ].
    toRemove do: [ :each | enemies remove: each ifAbsent: [] ]
