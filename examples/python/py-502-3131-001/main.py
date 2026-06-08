
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Конвертер °C → °F")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Температура в °C")

        self.result = QLabel("— ")

        btn = QPushButton("Перевести")
        btn.clicked.connect(self.convert)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(btn)
        layout.addWidget(self.result)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def convert(self) -> None:
        text = self.input.text().strip().replace(",", ".")
        try:
            c = float(text)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите число")
            return
        f = c * 9 / 5 + 32
        self.result.setText(f"{c:.1f} °C = {f:.1f} °F")


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(320, 160)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
