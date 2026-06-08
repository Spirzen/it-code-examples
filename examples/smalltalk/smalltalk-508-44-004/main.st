initializeWithGame: aGame
    super initialize.
    game := aGame.
    self buildStars

buildStars
    | extent |
    extent := game fieldExtent.
    stars := OrderedCollection new.
    80 timesRepeat: [
        stars add: {
            extent x atRandom.
            extent y atRandom.
            (0.2 + (0.8 atRandom)).
            (1 + 2 atRandom)
        } ]
