
import tkinter as tk

root = tk.Tk()

text_long = "Это длинный текст для демонстрации выравнивания.\nОн занимает несколько строк."

# Выравнивание содержимого внутри метки
label1 = tk.Label(root, text=text_long, justify="left", anchor="w", width=40, bg="lightblue")
label1.pack(fill="x", padx=10, pady=5)

# Выравнивание самой метки в контейнере
label2 = tk.Label(root, text="Центр", width=10, bg="lightgreen")
label2.pack(anchor="center", pady=5)

label3 = tk.Label(root, text="Право", width=10, bg="lightyellow")
label3.pack(anchor="e", pady=5)

root.mainloop()
