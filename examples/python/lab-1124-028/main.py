import tkinter as tk
from tkinter import messagebox

RATES = {"USD": 1.0, "EUR": 0.92, "RUB": 92.5}

def convert():
    try:
        amount = float(amount_var.getreplace(",", "."))
        src = from_var.get()
        dst = to_var.get()
        result = amount * RATES[dst] / RATES[src]
        result_var.set(f"{result:.2f} {dst}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректную сумму")

root = tk.Tk()
root.title("Конвертер валют")
root.resizable(False, False)

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

amount_var = tk.StringVar(value="100")
from_var = tk.StringVar(value="USD")
to_var = tk.StringVar(value="RUB")

tk.Label(frame, text="Сумма:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=amount_var, width=12).grid(row=0, column=1, padx=(8, 0))

tk.Label(frame, text="Из:").grid(row=1, column=0, sticky="w", pady=(8, 0))
from_menu = tk.OptionMenu(frame, from_var, *RATES.keys())
from_menu.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=(8, 0))

tk.Label(frame, text="В:").grid(row=2, column=0, sticky="w", pady=(8, 0))
to_menu = tk.OptionMenu(frame, to_var, *RATES.keys())
to_menu.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(8, 0))

result_var = tk.StringVar(value="—")
tk.Label(frame, textvariable=result_var, font=("Segoe UI", 12)).grid(
    row=3, column=0, columnspan=2, pady=(12, 0)
)
tk.Button(frame, text="Конвертировать", command=convert).grid(row=4, column=0, columnspan=2, pady=(12, 0))

root.mainloop()
