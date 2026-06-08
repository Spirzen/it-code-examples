
import tkinter as tk

def switch_image():
    global current_img
    if current_img == photo1:
        label.config(image=photo2)
        current_img = photo2
    else:
        label.config(image=photo1)
        current_img = photo1

root = tk.Tk()

photo1 = tk.PhotoImage(file="img1.gif")
photo2 = tk.PhotoImage(file="img2.gif")
current_img = photo1

label = tk.Label(root, image=photo1)
label.pack(pady=20)
label.bind("<Button-1>", lambda e: switch_image())

root.mainloop()
