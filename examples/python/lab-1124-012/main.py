import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Таблица")
root.geometry("320x220")

cols = ("name", "age")
tree = ttk.Treeview(root, columns=cols, show="headings", height=8)
tree.heading("name", text="Имя")
tree.heading("age", text="Возраст")
tree.column("age", width=60, anchor="center")
tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

for row in (("Алиса", 30), ("Боб", 25), ("Карл", 28)):
    tree.insert("", tk.END, values=row)

root.mainloop()
