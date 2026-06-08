
import tkinter as tk
import turtle

root = tk.Tk()
root.title("Turtle in Tkinter")

frame = tk.Frame(root)
frame.pack(side=tk.TOP)

def draw_square():
    t.clear()
    for _ in range(4):
        t.fd(100); t.rt(90)

btn = tk.Button(frame, text="Квадрат", command=draw_square)
btn.pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

ts = turtle.TurtleScreen(canvas)
ts.bgcolor("white")
t = turtle.RawTurtle(ts)
t.speed(0)

root.mainloop()
