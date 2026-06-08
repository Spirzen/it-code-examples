# include <Siv3D.hpp>

void Main()
{
    Scene scene{800, 600};
    const Font font{48};

    while (System::Update())
    {
        scene.draw(ColorF{0.12, 0.12, 0.16});
        scene.circle(400, 300, 50).draw(ColorF{0.3, 0.85, 0.5});
        font(U"Hello, Siv3D!").drawAt(400, 80, Palette::White);
    }
}
