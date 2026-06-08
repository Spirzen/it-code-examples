import tkinter as tk
from tkinter import ttk

def tick():
    value = progress["value"]
    if value < 100:
        progress["value"] = value + 5
        root.after(120, tick)  # следующий шаг через 120 мс

root = tk.Tk()
root.title("Прогресс")
root.geometry("320x100")

progress = ttk.Progressbar(root, length=260, mode="determinate")
progress.pack(pady=24)
progress["value"] = 0
tick()

root.mainloop()
