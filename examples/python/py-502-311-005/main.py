
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Наведи на меня", bg="lightgray", width=20, height=5)
label.pack(pady=50)

def on_enter(event):
    label.config(bg="lightblue", text="Я здесь")

def on_leave(event):
    label.config(bg="lightgray", text="Наведи на меня")

def on_click(event):
    label.config(text="Клик зарегистрирован", bg="lightgreen")

label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)
label.bind("<Button-1>", on_click)

root.mainloop()
