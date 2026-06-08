#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib demo");
    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        if (IsKeyPressed(KEY_ESCAPE))
            break;

        BeginDrawing();
        ClearBackground({30, 30, 40, 255});
        DrawCircle(400, 300, 50, {80, 200, 120, 255});
        DrawText("Hello, Raylib!", 280, 80, 28, RAYWHITE);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}
