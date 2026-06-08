    keys = pygame.key.get_pressed()
    soft_drop = keys[pygame.K_DOWN]

    if soft_drop:
        # Отдельный быстрый таймер soft drop (~0.05 с)
        if gravity_timer >= 0.05:
            if active.try_move(board, 0, 1):
                score += S.SOFT_DROP_BONUS
            gravity_timer = 0.0
    else:
        interval = GRAVITY_INTERVAL
        if gravity_timer >= interval:
            gravity_timer = 0.0
            active.try_move(board, 0, 1)
