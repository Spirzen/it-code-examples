import tkinter as tk

root = tk.Tk()
root.title("Длинная форма")
root.geometry("320x240")

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scroll_frame = tk.Frame(canvas)

scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
)

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

for i in range(20):
    tk.Label(scroll_frame, text=f"Поле {i + 1}").pack(anchor="w", padx=12, pady=2)
    tk.Entry(scroll_frame, width=30).pack(padx=12, pady=(0, 8))

root.mainloop()
