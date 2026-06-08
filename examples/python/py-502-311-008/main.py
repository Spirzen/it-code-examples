
import tkinter as tk

def countdown(count):
    label_text.set(f"Осталось: {count}")
    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        label_text.set("Время вышло")

root = tk.Tk()
root.geometry("300x200")

label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text, font=("Arial", 24))
label.pack(pady=50)

countdown(10)

root.mainloop()
