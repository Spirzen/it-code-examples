state = "MENU"
winner = ""

# KEYDOWN:
elif event.key == pygame.K_p and state in ("PLAYING", "PAUSED", "SERVE"):
    state = "PAUSED" if state == "PLAYING" else "PLAYING"
elif event.key == pygame.K_r and state == "WIN":
    score_left = score_right = 0
    ball.reset(center=True)
    state = "MENU"
elif event.key == pygame.K_SPACE:
    if state == "MENU":
        score_left = score_right = 0
        serve_direction = 1
        ball.reset(center=True)
        state = "SERVE"
    elif state == "SERVE":
        ball.reset(center=False, direction=serve_direction)
        state = "PLAYING"

# после гола:
if score_left >= S.WIN_SCORE:
    state = "WIN"
    winner = "Игрок 1"
elif score_right >= S.WIN_SCORE:
    state = "WIN"
    winner = "Игрок 2"

# draw:
draw_score(screen, score_left, score_right)
if state == "MENU":
    draw_menu(screen)
elif state == "PAUSED":
    draw_paused(screen)
elif state == "WIN":
    draw_win(screen, winner)
