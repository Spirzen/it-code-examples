import tkinter as tk

def append_digit(d):
    display_var.set(display_var.get() + d)

def clear():
    display_var.set("")

def calculate():
    try:
        display_var.set(str(eval(display_var.get())))
    except Exception:
        display_var.set("Ошибка")

root = tk.Tk()
root.title("Калькулятор")
root.resizable(False, False)

display_var = tk.StringVar(value="")
entry = tk.Entry(root, textvariable=display_var, justify="right", font=("Consolas", 16), width=14)
entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="ew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, row, col in buttons:
    cmd = clear if text == "C" else calculate if text == "=" else lambda t=text: append_digit(t)
    tk.Button(root, text=text, width=5, height=2, command=cmd).grid(row=row, column=col, padx=2, pady=2)

root.mainloop()
