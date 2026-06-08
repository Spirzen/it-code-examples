#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include "counter.hpp"

int main(int argc, char* argv[]) {
    QGuiApplication app(argc, argv);

    Counter counter;

    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("counter", &counter);
    engine.loadFromModule("HelloApp", "Main");

    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}
