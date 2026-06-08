import tkinter as tk

root = tk.Tk()
root.title("Canvas")
root.geometry("320x240")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

canvas.create_rectangle(30, 30, 130, 100, fill="lightblue", outline="navy")
canvas.create_oval(160, 40, 260, 140, fill="lightgreen", outline="darkgreen")
canvas.create_line(30, 160, 290, 160, fill="gray", width=2)
canvas.create_text(160, 190, text="Tkinter Canvas", font=("Segoe UI", 11))

root.mainloop()
