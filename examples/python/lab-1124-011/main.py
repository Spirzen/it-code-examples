import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox")
root.geometry("280x120")

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

tk.Label(frame, text="Категория:").grid(row=0, column=0, sticky="w")
combo = ttk.Combobox(
    frame,
    values=["Работа", "Личное", "Учёба"],
    state="readonly",  # только выбор из списка, без произвольного текста
    width=18,
)
combo.set("Работа")
combo.grid(row=0, column=1, padx=(8, 0))

status = tk.StringVar(value=f"Выбрано: {combo.get()}")
combo.bind("<<ComboboxSelected>>", lambda e: status.set(f"Выбрано: {combo.get()}"))
tk.Label(frame, textvariable=status, fg="gray").grid(row=1, column=0, columnspan=2, pady=(12, 0))

root.mainloop()
