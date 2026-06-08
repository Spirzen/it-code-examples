import tkinter as tk

root = tk.Tk()
root.title("Рисовалка")
root.geometry("400x320")

canvas = tk.Canvas(root, bg="white", cursor="crosshair")
canvas.pack(fill=tk.BOTH, expand=True)

color = {"value": "black"}

def set_color(c):
    color["value"] = c

def paint(event):
    x, y = event.x, event.y
    r = 3
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color["value"], outline=color["value"])

canvas.bind("<B1-Motion>", paint)

toolbar = tk.Frame(root)
toolbar.pack(fill=tk.X, padx=8, pady=4)
for c, name in (("black", "Чёрный"), ("red", "Красный"), ("blue", "Синий")):
    tk.Button(toolbar, text=name, command=lambda col=c: set_color(col)).pack(side=tk.LEFT, padx=2)
tk.Button(toolbar, text="Очистить", command=lambda: canvas.delete("all")).pack(side=tk.RIGHT)

root.mainloop()
