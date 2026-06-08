import tkinter as tk
from tkinter import messagebox

def greet():
    name = entry.getstrip()  # get() — текст из поля; strip() убирает пробелы по краям
    if name:
        messagebox.showinfo("Привет", f"Здравствуй, {name}!")
    else:
        messagebox.showwarning("Пусто", "Введите имя")

root = tk.Tk()
root.title("Приветствие")
root.resizable(False, False)  # запрет изменения размера окна

frame = tk.Frame(root, padx=16, pady=16)  # Frame — контейнер для группы виджетов
frame.pack()

tk.Label(frame, text="Ваше имя:").grid(row=0, column=0, sticky="w")
entry = tk.Entry(frame, width=24)
entry.grid(row=0, column=1, padx=(8, 0))
entry.focus_set()  # курсор сразу в поле
entry.bind("<Return>", lambda e: greet())  # Enter = тот же greet()

tk.Button(frame, text="Приветствовать", command=greet).grid(
    row=1, column=0, columnspan=2, pady=(12, 0)
)

root.mainloop()
