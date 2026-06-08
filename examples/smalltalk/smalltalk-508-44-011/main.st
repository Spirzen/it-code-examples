updateEnemies
    | toRemove enemy type size speed shootTimer x y phase dx |
    toRemove := OrderedCollection new.
    speed := self enemySpeed.
    enemies do: [ :each |
        enemy := each.
        type := enemy third.
        size := self enemySizeFor: type.
        x := enemy first.
        y := enemy second + speed.
        phase := enemy sixth.
        type = #zigzag ifTrue: [
            dx := (phase sin * 2.5) asInteger.
            x := (x + dx) max: 0 min: fieldWidth - size x ].
        enemy at: 1 put: x.
        enemy at: 2 put: y.
        (y > fieldHeight + 40) ifTrue: [
            toRemove add: enemy.
            self damagePlayer ].
        type = #shooter ifTrue: [
            shootTimer := enemy fifth - 1.
            enemy at: 5 put: shootTimer.
            shootTimer <= 0 ifTrue: [
                self addEnemyBulletAt: (x + (size x // 2) - 2) @ (y + size y).
                enemy at: 5 put: (100 + 80 atRandom) - (waveNumber * 2 max: 0) ] ] ].
    toRemove do: [ :each | enemies remove: each ifAbsent: [] ]
