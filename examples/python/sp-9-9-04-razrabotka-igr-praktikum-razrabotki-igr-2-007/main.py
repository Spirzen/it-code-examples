def main():
    game = Match3Game()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.on_mouse_down(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                game.on_mouse_move(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                game.on_mouse_up(event.pos)
        game.update()
        game.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
