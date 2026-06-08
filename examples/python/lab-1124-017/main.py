import tkinter as tk
from tkinter import filedialog, colorchooser

def open_file():
    path = filedialog.askopenfilename(filetypes=[("Текст", "*.txt"), ("Все", "*.*")])
    if path:
        status_var.set(f"Открыт: {path}")

def pick_color():
    result = colorchooser.askcolor()
    if result[1]:
        root.configure(bg=result[1])
        status_var.set(f"Фон: {result[1]}")

root = tk.Tk()
root.title("Диалоги")
root.geometry("360x160")

status_var = tk.StringVar(value="Готово")
tk.Label(root, textvariable=status_var).pack(pady=(16, 8))

btn_row = tk.Frame(root)
btn_row.pack()
tk.Button(btn_row, text="Открыть файл", command=open_file).pack(side=tk.LEFT, padx=4)
tk.Button(btn_row, text="Цвет фона", command=pick_color).pack(side=tk.LEFT, padx=4)
tk.Button(btn_row, text="Выход", command=root.destroy).pack(side=tk.LEFT, padx=4)

root.mainloop()
