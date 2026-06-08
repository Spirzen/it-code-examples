import tkinter as tk

root = tk.Tk()
root.title("Toolbar")

toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

for label in ("Новый", "Открыть", "Сохранить", "Выход"):
    tk.Button(toolbar, text=label, padx=8, pady=4).pack(side=tk.LEFT, padx=2, pady=2)

content = tk.Label(root, text="Область документа", bg="white")
content.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

root.mainloop()
