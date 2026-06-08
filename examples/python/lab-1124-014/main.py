import tkinter as tk
from tkinter import messagebox

def about():
    messagebox.showinfo("О программе", "Пример меню на Tkinter")

root = tk.Tk()
root.title("Меню")

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Новый", command=lambda: print("Новый"))
file_menu.add_command(label="Открыть", command=lambda: print("Открыть"))
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.destroy)
menubar.add_cascade(label="Файл", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="О программе", command=about)
menubar.add_cascade(label="Справка", menu=help_menu)

root.config(menu=menubar)
tk.Label(root, text="Выберите пункт меню сверху").pack(expand=True)

root.mainloop()
