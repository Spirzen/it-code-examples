import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk-тема")

style = ttk.Style()
style.theme_use("clam")  # попробуйте vista, xpnative на Windows

frame = ttk.Frame(root, padding=16)
frame.pack()

ttk.Label(frame, text="Современный вид ttk").pack(pady=(0, 8))
ttk.Button(frame, text="OK").pack(pady=4)
ttk.Checkbutton(frame, text="Запомнить").pack(pady=4)

root.mainloop()
