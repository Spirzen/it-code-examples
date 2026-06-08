
import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()

custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

label = tk.Label(root, text="Стильный текст", font=custom_font)
label.pack()

# Получение метрик
metrics = custom_font.metrics()
print(metrics)

root.mainloop()
