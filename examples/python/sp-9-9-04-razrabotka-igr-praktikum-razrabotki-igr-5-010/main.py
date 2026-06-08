def tick_gravity(board, active, gravity_timer, dt, level, score_ref):
    """
    score_ref — список [score], чтобы менять счёт из функции.
    Возвращает (active, gravity_timer, locked).
    """
    keys = pygame.key.get_pressed()
    soft_drop = keys[pygame.K_DOWN]
    gravity_timer += dt
    locked = False

    interval = S.SOFT_DROP_INTERVAL if soft_drop else gravity_interval(level)

    if gravity_timer >= interval:
        gravity_timer = 0.0
        if active.try_move(board, 0, 1):
            if soft_drop:
                score_ref[0] += S.SOFT_DROP_BONUS
        else:
            lock_piece(board, active)
            locked = True

    return active, gravity_timer, locked
