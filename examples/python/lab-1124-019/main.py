import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Вкладки")
root.geometry("360x220")

notebook = ttk.Notebook(root)
tab_general = ttk.Frame(notebook, padding=12)
tab_advanced = ttk.Frame(notebook, padding=12)
notebook.add(tab_general, text="Общее")
notebook.add(tab_advanced, text="Дополнительно")
notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

tk.Label(tab_general, text="Имя приложения:").grid(row=0, column=0, sticky="w")
tk.Entry(tab_general, width=24).grid(row=0, column=1, padx=(8, 0))

tk.Label(tab_advanced, text="Порт сервера:").grid(row=0, column=0, sticky="w")
tk.Entry(tab_advanced, width=10).grid(row=0, column=1, padx=(8, 0))

root.mainloop()
