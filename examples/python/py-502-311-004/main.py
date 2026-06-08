
import tkinter as tk

root = tk.Tk()

text_var = tk.StringVar()
text_var.set("Начальное значение")

label = tk.Label(root, textvariable=text_var)
label.pack()

def update_text():
    text_var.set("Обновлённый текст")

button = tk.Button(root, text="Изменить", command=update_text)
button.pack()

root.mainloop()
