
import tkinter as tk

root = tk.Tk()

label_title = tk.Label(
    root,
    text="Заголовок окна",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="black",
    padx=20,
    pady=10
)
label_title.pack(pady=20)

label_info = tk.Label(
    root,
    text="Это информационная метка.\nТекст может быть многострочным.",
    justify="left",
    wraplength=200
)
label_info.pack()

root.mainloop()
