#pragma once
#include <QObject>

class Counter : public QObject {
    Q_OBJECT
    Q_PROPERTY(int value READ value WRITE setValue NOTIFY valueChanged)
public:
    explicit Counter(QObject* parent = nullptr) : QObject(parent) {}

    int value() const { return value_; }
    void setValue(int v) {
        if (value_ == v) return;
        value_ = v;
        emit valueChanged();
    }

    Q_INVOKABLE void increment() { setValue(value_ + 1); }

signals:
    void valueChanged();

private:
    int value_{0};
};
