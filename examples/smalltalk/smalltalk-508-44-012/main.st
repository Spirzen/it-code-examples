drawOn: aCanvas
    | star x y alpha size enemy type enemySize bullet isPlayer blink |
    super drawOn: aCanvas.
    aCanvas fillRectangle: self bounds color: (Color r: 0.02 g: 0.04 b: 0.12).
    stars do: [ :each |
        star := each.
        x := star first.
        y := (star second + (game score \\ 640)) \\ (game fieldExtent y).
        alpha := star third.
        size := star fourth.
        aCanvas fillOval: (x @ y extent: size @ size) color: (Color white alpha: alpha) ].
    game enemiesList do: [ :enemy |
        type := enemy third.
        enemySize := game enemySizeFor: type.
        x := enemy first.
        y := enemy second.
        type = #grunt ifTrue: [
            aCanvas fillRectangle: (x @ y extent: enemySize) color: Color red ].
        type = #zigzag ifTrue: [
            aCanvas fillRectangle: (x @ y extent: enemySize) color: (Color r: 1.0 g: 0.5 b: 0.1).
            aCanvas fillRectangle: ((x + 4) @ (y + 4) extent: (enemySize x - 8) @ (enemySize y - 8)) color: (Color r: 0.15 g: 0.05 b: 0.05) ].
        type = #shooter ifTrue: [
            aCanvas fillRectangle: (x @ y extent: enemySize) color: (Color r: 0.7 g: 0.2 b: 1.0).
            aCanvas fillRectangle: ((x + 6) @ (y + enemySize y - 6) extent: 14 @ 4) color: Color yellow ] ].
    game bulletsList do: [ :bullet |
        isPlayer := bullet fifth.
        x := bullet first.
        y := bullet second.
        isPlayer
            ifTrue: [ aCanvas fillRectangle: (x @ y extent: 4 @ 10) color: Color yellow ]
            ifFalse: [ aCanvas fillOval: (x @ y extent: 6 @ 6) color: (Color orange red: 1.0 green: 0.4 blue: 0.1) ] ].
    x := game playerOrigin x.
    y := game playerOrigin y.
    blink := game invulnerable and: [ (game tickCount bitAnd: 4) = 0 ].
    blink ifFalse: [
        aCanvas fillRectangle: (x @ y extent: game playerSize) color: (Color r: 0.2 g: 0.9 b: 1.0).
        aCanvas fillRectangle: ((x + 4) @ (y + 6) extent: 20 @ 8) color: (Color r: 0.05 g: 0.3 b: 0.5).
        aCanvas fillRectangle: ((x + 10) @ (y - 4) extent: 8 @ 6) color: Color white ]
