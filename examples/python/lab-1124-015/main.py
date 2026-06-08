import tkinter as tk

root = tk.Tk()
root.title("StatusBar")
root.geometry("360x200")

content = tk.Label(root, text="Основная область", bg="white")
content.pack(fill=tk.BOTH, expand=True)

status_var = tk.StringVar(value="Готово")
statusbar = tk.Label(
    root,
    textvariable=status_var,
    bd=1,
    relief=tk.SUNKEN,
    anchor=tk.W,
    padx=8,
)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

def simulate_save():
    status_var.set("Сохранение..")
    root.after(800, lambda: status_var.set("Файл сохранён"))  # через 800 мс

tk.Button(root, text="Сохранить", command=simulate_save).pack(pady=8)

root.mainloop()
