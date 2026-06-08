
import tkinter as tk

from tkinter import messagebox


def convert():
    raw = entry.get().strip().replace(",", ".")
    try:
        celsius = float(raw)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите число, например 25")
        return
    fahrenheit = celsius * 9 / 5 + 32
    result_var.set(f"{celsius:.1f} °C = {fahrenheit:.1f} °F")


root = tk.Tk()
root.title("Конвертер температуры")
root.resizable(False, False)

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

tk.Label(frame, text="Температура (°C):").grid(row=0, column=0, sticky="w")
entry = tk.Entry(frame, width=12)
entry.grid(row=0, column=1, padx=(8, 0))
entry.focus_set()

result_var = tk.StringVar(value="— ")
tk.Label(frame, textvariable=result_var).grid(row=1, column=0, columnspan=2, pady=(12, 0))

btn_row = tk.Frame(frame)
btn_row.grid(row=2, column=0, columnspan=2, pady=(12, 0))
tk.Button(btn_row, text="Перевести", command=convert).pack(side=tk.LEFT, padx=4)
tk.Button(btn_row, text="Выход", command=root.destroy).pack(side=tk.LEFT, padx=4)

entry.bind("<Return>", lambda _e: convert())

root.mainloop()
