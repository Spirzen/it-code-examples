        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif state == STATE_MENU and event.key == pygame.K_SPACE:
                state = STATE_PLAYING
                board = new_board()
                score = lines_total = level = 0
                gravity_timer = 0.0
                next_kind = random_kind()
                active = spawn_piece(next_kind)
                next_kind = random_kind()
            elif state == STATE_PLAYING and event.key == pygame.K_p:
                state = STATE_PAUSED
            elif state == STATE_PAUSED and event.key == pygame.K_p:
                state = STATE_PLAYING
            elif state == STATE_GAME_OVER and event.key == pygame.K_r:
                state = STATE_MENU
