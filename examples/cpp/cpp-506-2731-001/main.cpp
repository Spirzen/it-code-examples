#include <QApplication>
#include <QPushButton>
#include <QVBoxLayout>
#include <QWidget>
#include <QLabel>

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);

    QWidget window;
    window.setWindowTitle("Qt Hello");

    auto* label = new QLabel("Нажмите кнопку", &window);
    auto* button = new QPushButton("Click", &window);

    QObject::connect(button, &QPushButton::clicked, [label]() {
        label->setText("Привет из Qt!");
    });

    auto* layout = new QVBoxLayout(&window);
    layout->addWidget(label);
    layout->addWidget(button);

    window.resize(320, 120);
    window.show();

    return app.exec();
}
