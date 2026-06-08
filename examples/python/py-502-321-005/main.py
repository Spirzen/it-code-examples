def dragon_curve(iterations=12):
    # Направления: 0=вправо, 1=вверх, 2=влево, 3=вниз
    turns = []
    for i in range(iterations):
        rev = [1 - x for x in reversed(turns)]  # инверсия
        turns = turns + [0] + rev
    
    t.fd(5)
    for turn in turns:
        if turn == 0:
            t.rt(90)
        else:
            t.lt(90)
        t.fd(5)
