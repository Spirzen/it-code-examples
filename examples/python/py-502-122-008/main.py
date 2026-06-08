
import tkinter as tk

def on_click():
    label.config(text="Кнопка нажата")

app = tk.Tk()
app.title("Пример tkinter")
app.geometry("300x150")

label = tk.Label(app, text="Нажмите кнопку")
label.pack(pady=10)

button = tk.Button(app, text="Нажать", command=on_click)
button.pack()

app.mainloop()
