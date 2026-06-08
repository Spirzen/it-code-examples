
import tkinter as tk

root = tk.Tk()

var = tk.IntVar()
var.set(10)

label = tk.Label(root, textvariable=var)
label.pack()

def increment():
    current = var.get()
    var.set(current + 1)

button = tk.Button(root, text="+", command=increment)
button.pack()

root.mainloop()
