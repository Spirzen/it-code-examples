updateWaves
    waveState = #break ifTrue: [
        waveBreakTimer := waveBreakTimer - 1.
        waveBreakTimer <= 0 ifTrue: [
            self beginWave ] ].
    waveState = #spawning ifTrue: [
        spawnDelayTimer := spawnDelayTimer - 1.
        spawnDelayTimer <= 0 ifTrue: [
            self spawnNextEnemy.
            spawnDelayTimer := 5 ].
        spawnIndex > spawnQueue size ifTrue: [
            waveState := #fighting ] ]

beginWave
    waveNumber := waveNumber + 1.
    spawnQueue := self buildSpawnQueue.
    spawnIndex := 1.
    spawnDelayTimer := 0.
    waveState := #spawning

buildSpawnQueue
    | count queue spacing i pattern row |
    queue := OrderedCollection new.
    count := (waveNumber + 3) min: 18.
    pattern := waveNumber \\ 4.
    pattern = 0 ifTrue: [
        spacing := fieldWidth // (count + 1).
        1 to: count do: [ :n |
            queue add: (spacing * n) @ -30 ] ].
    pattern = 1 ifTrue: [
        spacing := fieldWidth // (count + 1).
        1 to: count do: [ :n |
            row := (n - 1) \\ 3.
            queue add: (spacing * n) @ (-30 - (row * 28)) ] ].
    pattern = 2 ifTrue: [
        1 to: count do: [ :n |
            queue add: (40 + ((fieldWidth - 80) * (n - 1) / (count - 1 max: 1)) asInteger) @ -30 ] ].
    pattern = 3 ifTrue: [
        1 to: count do: [ :n |
            i := n - 1.
            queue add: ((fieldWidth // 2) + ((i - (count // 2)) * 36)) @ (-30 - (i abs * 12)) ] ].
    ^ queue

spawnNextEnemy
    | point |
    spawnIndex > spawnQueue size ifTrue: [ ^ self ].
    point := spawnQueue at: spawnIndex.
    self addEnemyAt: point type: self randomEnemyType.
    spawnIndex := spawnIndex + 1

checkWaveComplete
    (enemies isEmpty and: [ waveState = #fighting ]) ifTrue: [
        waveState := #break.
        waveBreakTimer := 90 ]
