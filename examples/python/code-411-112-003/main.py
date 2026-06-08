# settings_demo.py

import sys
import os

from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtCore import QSettings, QStandardPaths

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки с QSettings")

        # Инициализация QSettings:
        # - organization — имя организации (для разделения настроек разных приложений)
        # - application — имя приложения
        # Хранится в реестре (Windows), plist (macOS) или ~/.config (Linux)
        self.settings = QSettings("МояОрганизация", "ДемоНастроек")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.select_button = QPushButton("Выбрать папку")
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.status_label = QPushButton("Последняя папка: (не выбрана)")
        self.status_label.setEnabled(False)
        layout.addWidget(self.status_label)

        self.central_widget.setLayout(layout)

        # Загрузка сохранённого значения при старте
        last_path = self.settings.value("last_folder", "")
        if last_path and os.path.isdir(last_path):
            self.status_label.setText(f"Последняя папка: {last_path}")

    def select_folder(self):
        # Получаем последний путь из настроек (или домашнюю директорию по умолчанию)
        last_path = self.settings.value("last_folder", 
                                       QStandardPaths.writableLocation(QStandardPaths.HomeLocation))

        folder = QFileDialog.getExistingDirectory(
            self, 
            "Выберите папку", 
            last_path  # Начинаем с последнего сохранённого пути
        )

        if folder:
            # Сохраняем путь в настройки
            self.settings.setValue("last_folder", folder)
            self.status_label.setText(f"Последняя папка: {folder}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
