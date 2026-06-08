import tkinter as tk

def on_change(value):
    volume_var.set(f"Громкость: {int(float(value))}%")

root = tk.Tk()
root.title("Ползунок")

volume_var = tk.StringVar(value="Громкость: 50%")
tk.Label(root, textvariable=volume_var, font=("Segoe UI", 12)).pack(pady=(20, 8))

scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=260,
    command=on_change,  # value приходит строкой, например "50.0"
)
scale.set(50)
scale.pack(padx=20, pady=(0, 20))

root.mainloop()
