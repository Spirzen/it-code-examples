Camera3D camera = { 0 };
camera.position = {4.f, 4.f, 4.f};
camera.target = {0.f, 0.f, 0.f};
camera.up = {0.f, 1.f, 0.f};
camera.fovy = 45.f;
camera.projection = CAMERA_PERSPECTIVE;

while (!WindowShouldClose()) {
    UpdateCamera(&camera, CAMERA_ORBITAL);
    BeginDrawing();
    ClearBackground(RAYWHITE);
    BeginMode3D(camera);
    DrawCube({0, 0, 0}, 2, 2, 2, RED);
    DrawGrid(10, 1.f);
    EndMode3D();
    EndDrawing();
}
