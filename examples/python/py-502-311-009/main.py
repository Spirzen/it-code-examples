
import tkinter as tk

root = tk.Tk()
root.config(bg="gray")

label = tk.Label(
    root,
    text="Эффектная метка",
    font=("Arial", 16),
    bg="white",
    fg="black",
    padx=20,
    pady=10,
    relief="raised",
    borderwidth=4
)
label.pack(pady=50)

root.mainloop()
