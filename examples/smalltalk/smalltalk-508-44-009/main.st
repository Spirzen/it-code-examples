checkCollisions
    | playerRect bulletRect enemyRect size points deadBullets deadEnemies killedEnemies |
    playerRect := playerX @ playerY extent: playerWidth @ playerHeight.
    deadBullets := OrderedCollection new.
    deadEnemies := OrderedCollection new.
    killedEnemies := Set new.
    bullets do: [ :bullet |
        bullet fifth ifTrue: [
            bulletRect := bullet first @ bullet second extent: 4 @ 10.
            enemies do: [ :enemy |
                (killedEnemies includes: enemy) ifFalse: [
                    size := self enemySizeFor: enemy third.
                    enemyRect := enemy first @ enemy second extent: size.
                    (bulletRect intersects: enemyRect) ifTrue: [
                        deadBullets add: bullet.
                        enemy at: 4 put: (enemy fourth - 1).
                        (enemy fourth <= 0) ifTrue: [
                            killedEnemies add: enemy.
                            deadEnemies add: enemy.
                            points := enemy third = #shooter
                                ifTrue: [ 150 ]
                                ifFalse: [ enemy third = #zigzag ifTrue: [ 75 ] ifFalse: [ 50 ] ].
                            score := score + points ] ] ] ] ] ].
    enemies do: [ :enemy |
        size := self enemySizeFor: enemy third.
        enemyRect := enemy first @ enemy second extent: size.
        (invulnerableTimer <= 0 and: [ enemyRect intersects: playerRect ]) ifTrue: [
            deadEnemies add: enemy.
            self damagePlayer ] ].
    deadBullets do: [ :each | bullets remove: each ifAbsent: [] ].
    deadEnemies do: [ :each | enemies remove: each ifAbsent: [] ]
