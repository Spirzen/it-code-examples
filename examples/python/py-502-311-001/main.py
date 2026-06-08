
import tkinter as tk

from tkinter import messagebox

root = tk.Tk()
root.title("Пример GUI")
root.geometry("300x200")

label = tk.Label(root, text="Введите имя:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

def greet():
    name = entry.get()
    messagebox.showinfo("Приветствие", f"Привет, {name}!")

button = tk.Button(root, text="Приветствовать", command=greet)
button.pack(pady=10)

root.mainloop()
