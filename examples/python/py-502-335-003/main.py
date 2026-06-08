"""GUI-приложение: рисуйте цифру мышью, PyTorch распознаёт её."""

import tkinter as tk
from tkinter import ttk

import torch

from model import DigitCNN
from train import MODEL_PATH

CANVAS_SIZE = 280


class DigitRecognizerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Распознавание цифр — PyTorch")
        self.root.resizable(False, False)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model: DigitCNN | None = None

        self._build_ui()

        if MODEL_PATH.exists():
            self._load_model()
        else:
            self.result_var.set("Сначала выполните: python train.py")

    def _build_ui(self) -> None:
        main = ttk.Frame(self.root, padding=16)
        main.grid(row=0, column=0)

        ttk.Label(main, text="Нарисуйте цифру от 0 до 9", font=("Segoe UI", 14)).grid(
            row=0, column=0, columnspan=2, pady=(0, 12)
        )

        self.canvas = tk.Canvas(
            main,
            width=CANVAS_SIZE,
            height=CANVAS_SIZE,
            bg="black",
            highlightthickness=2,
            highlightbackground="#cccccc",
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        btn_frame = ttk.Frame(main)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=12)

        self.predict_btn = ttk.Button(btn_frame, text="Распознать", state=tk.DISABLED)
        self.predict_btn.pack(side=tk.LEFT, padx=4)
        ttk.Button(btn_frame, text="Очистить", command=self._clear).pack(side=tk.LEFT, padx=4)

        self.result_var = tk.StringVar(value="Загрузка...")
        ttk.Label(main, textvariable=self.result_var, font=("Segoe UI", 12)).grid(
            row=3, column=0, columnspan=2
        )

        ttk.Label(
            main,
            text=f"PyTorch · {self.device}",
            font=("Segoe UI", 9),
            foreground="#666666",
        ).grid(row=4, column=0, columnspan=2, pady=(8, 0))

    def _load_model(self) -> None:
        model = DigitCNN().to(self.device)
        model.load_state_dict(torch.load(MODEL_PATH, map_location=self.device, weights_only=True))
        model.eval()
        self.model = model
        self.result_var.set("Результат появится здесь")
        self.predict_btn.config(state=tk.NORMAL)

    def _clear(self) -> None:
        self.canvas.delete("all")


def main() -> None:
    root = tk.Tk()
    style = ttk.Style()
    if "vista" in style.theme_names():
        style.theme_use("vista")
    DigitRecognizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
