import tkinter as tk

root = tk.Tk()
root.title("Place")
root.geometry("300x200")

canvas = tk.Canvas(root, bg="#f0f0f0")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_rectangle(20, 20, 120, 80, fill="lightblue", outline="")
canvas.create_oval(140, 30, 220, 110, fill="lightgreen", outline="")
tk.Label(canvas, text="Метка", bg="#f0f0f0").place(x=30, y=100)

root.mainloop()
