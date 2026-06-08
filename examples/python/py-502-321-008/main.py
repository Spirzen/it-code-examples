
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

root = tk.Tk()
fig, ax = plt.subplots()
ax.plot([0,1,2], [0,1,0])
canvas_mpl = FigureCanvasTkAgg(fig, root)
canvas_mpl.get_tk_widget().pack(side=tk.LEFT)

canvas_turtle = tk.Canvas(root, width=400, height=300)
canvas_turtle.pack(side=tk.RIGHT)
ts = turtle.TurtleScreen(canvas_turtle)
t = turtle.RawTurtle(ts)
t.circle(50)
