bool running = true;
Player player{};
World world{};

while (running) {
    InputState input = poll_input();       // 1) Считать ввод
    running = !input.quit_requested;

    update_player(player, input, world);   // 2) Обновить состояние
    update_world(world);

    begin_frame();                         // 3) Отрисовать кадр
    draw_world(world);
    draw_player(player);
    end_frame();
}
