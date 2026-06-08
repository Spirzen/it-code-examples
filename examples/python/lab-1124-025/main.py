import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Горячие клавиши")
root.geometry("320x120")

status = tk.StringVar(value="Ctrl+S — сохранить, Ctrl+Q — выход")
tk.Label(root, textvariable=status).pack(expand=True)

def save(_=None):
    messagebox.showinfo("Сохранить", "Документ сохранён (демо)")

root.bind("<Control-s>", save)
root.bind("<Control-q>", lambda e: root.destroy())

root.mainloop()
