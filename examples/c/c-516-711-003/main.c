char current_player = 'X';
int game_over = 0;

while (!game_over) {
    print_board(board);
    make_move(board, current_player); // функция ввода и валидации

    if (check_winner(board, current_player)) {
        print_board(board);
        printf("Игрок %c победил!\n", current_player);
        game_over = 1;
    } else if (is_board_full(board)) {
        print_board(board);
        printf("Ничья!\n");
        game_over = 1;
    } else {
        current_player = (current_player == 'X') ? 'O' : 'X';
    }
}
