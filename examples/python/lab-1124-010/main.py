import tkinter as tk

def on_change(*_):
    count_var.set(f"Символов: {len(entry_var.get())}")

root = tk.Tk()
root.title("Счётчик")

entry_var = tk.StringVar()
entry_var.trace_add("write", on_change)  # следить за каждым изменением текста

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

tk.Entry(frame, textvariable=entry_var, width=40).pack()
count_var = tk.StringVar(value="Символов: 0")
tk.Label(frame, textvariable=count_var, fg="gray").pack(anchor="w", pady=(8, 0))

root.mainloop()
