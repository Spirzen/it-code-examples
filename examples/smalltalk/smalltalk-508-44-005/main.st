drawOn: aCanvas
    | star x y alpha size blink |
    super drawOn: aCanvas.
    aCanvas fillRectangle: self bounds color: (Color r: 0.02 g: 0.04 b: 0.12).
    stars do: [ :each |
        star := each.
        x := star first.
        y := (star second + (game score \\ 640)) \\ (game fieldExtent y).
        alpha := star third.
        size := star fourth.
        aCanvas fillOval: (x @ y extent: size @ size) color: (Color white alpha: alpha) ].
    x := game playerOrigin x.
    y := game playerOrigin y.
    blink := game invulnerable and: [ (game tickCount bitAnd: 4) = 0 ].
    blink ifFalse: [
        aCanvas fillRectangle: (x @ y extent: game playerSize) color: (Color r: 0.2 g: 0.9 b: 1.0).
        aCanvas fillRectangle: ((x + 4) @ (y + 6) extent: 20 @ 8) color: (Color r: 0.05 g: 0.3 b: 0.5).
        aCanvas fillRectangle: ((x + 10) @ (y - 4) extent: 8 @ 6) color: Color white ]
